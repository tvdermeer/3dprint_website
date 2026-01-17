<script setup>
import { ref, onMounted, watch, computed, nextTick } from 'vue'
import { RouterLink } from 'vue-router'
import { Trash2, ArrowLeft, CreditCard, Lock } from 'lucide-vue-next'
import { loadStripe } from '@stripe/stripe-js'
import { useCartStore } from '../stores/cart'
import { useThemeStore } from '../stores/theme'
import { ordersApi, paymentApi } from '../api/client'

const cartStore = useCartStore()
const themeStore = useThemeStore()
const step = ref('cart') // 'cart', 'payment', 'success'
const formData = ref({
  email: '',
  name: '',
  address: '',
  city: '',
  zipCode: '',
})

const shippingCost = 9.99
const taxRate = 0.08

const tax = computed(() => cartStore.totalPrice * taxRate)
const finalTotal = computed(() => cartStore.totalPrice + shippingCost + tax.value)

const handleInputChange = (e) => {
  const { name, value } = e.target
  formData.value[name] = value
}

// Stripe Setup
const stripe = ref(null)
const elements = ref(null)
const card = ref(null)
const stripeError = ref('')
const processing = ref(false)

const getStripeStyle = () => {
  const isDark = themeStore.theme === 'dark'
  return {
    base: {
      color: isDark ? '#fff' : '#111827',
      fontFamily: 'Inter, system-ui, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': {
        color: isDark ? '#9ca3af' : '#6b7280'
      }
    },
    invalid: {
      color: '#ef4444',
      iconColor: '#ef4444'
    }
  }
}

const initializeStripe = async () => {
  if (!stripe.value) {
    stripe.value = await loadStripe(import.meta.env.VITE_STRIPE_PUBLISHABLE_KEY)
  }
  
  if (stripe.value && step.value === 'payment' && !card.value) {
    elements.value = stripe.value.elements()
    
    const style = getStripeStyle()
    
    card.value = elements.value.create('card', { style })
    // Use nextTick to ensure the DOM element exists
    setTimeout(() => {
      const cardElement = document.getElementById('card-element')
      if (cardElement) {
        card.value.mount('#card-element')
        
        card.value.on('change', (event) => {
          stripeError.value = event.error ? event.error.message : ''
        })
      }
    }, 100)
  }
}

// Update Stripe style when theme changes
watch(() => themeStore.theme, () => {
  if (card.value) {
    card.value.update({ style: getStripeStyle() })
  }
})

// Watch for step changes to initialize stripe when payment step is reached
watch(step, (newStep) => {
  if (newStep === 'payment') {
    initializeStripe()
  }
})

const handlePlaceOrder = async (e) => {
  e.preventDefault()
  
  if (processing.value) return
  
  processing.value = true
  stripeError.value = ''
  
  try {
    // 1. Create PaymentIntent
    const { clientSecret } = await paymentApi.createIntent(finalTotal.value)
    
    // 2. Confirm Payment
    const result = await stripe.value.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card.value,
        billing_details: {
          name: formData.value.name,
          email: formData.value.email,
          address: {
            line1: formData.value.address,
            city: formData.value.city,
            postal_code: formData.value.zipCode,
            country: 'US'
          }
        }
      }
    })
    
    if (result.error) {
      throw new Error(result.error.message)
    }
    
    if (result.paymentIntent.status === 'succeeded') {
       // 3. Create Order
      // Prepare order items
      const orderItems = cartStore.items.map(item => ({
        product_id: item.id,
        quantity: item.quantity,
        price_at_purchase: item.price
      }))
      
      // Create order payload
      const orderData = {
        customer_email: formData.value.email,
        customer_name: formData.value.name,
        shipping_address: {
          line1: formData.value.address,
          city: formData.value.city,
          postal_code: formData.value.zipCode,
          country: 'US' // Defaulting to US for now
        },
        items: orderItems,
        total_amount: finalTotal.value
      }
      
      // Call API
      await ordersApi.create(orderData)
      
      step.value = 'success'
      setTimeout(() => {
        cartStore.clearCart()
      }, 3000)
    }
    
  } catch (error) {
    console.error('Failed to process payment:', error)
    stripeError.value = error.message || 'Payment failed. Please try again.'
  } finally {
    processing.value = false
  }
}
</script>

<template>
  <div class="min-h-dvh py-16 bg-bg-main transition-colors duration-300">
    <div class="container mx-auto">
      <div class="max-w-6xl mx-auto">
        <!-- Success Screen -->
        <div v-if="step === 'success'" class="max-w-2xl mx-auto">
          <div class="card text-center">
            <div class="size-16 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg class="size-8 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h1 class="text-4xl mb-4 text-text-main text-balance">Order Confirmed!</h1>
            <p class="text-xl text-text-muted mb-8 text-pretty">
              Thank you for your purchase. Your order has been successfully placed.
            </p>
            <p class="text-text-muted mb-8 text-pretty">
              You will receive a confirmation email shortly with tracking information.
            </p>
            <RouterLink
              to="/"
              class="btn-primary inline-flex items-center gap-2"
            >
              <ArrowLeft class="size-5" />
              Back to Home
            </RouterLink>
          </div>
        </div>

        <!-- Empty Cart -->
        <div v-else-if="cartStore.items.length === 0" class="max-w-2xl mx-auto">
          <div class="card text-center">
            <h1 class="text-4xl mb-4 text-text-main text-balance">Your Cart is Empty</h1>
            <p class="text-xl text-text-muted mb-8 text-pretty">
              Add some items to your cart to get started.
            </p>
            <RouterLink
              to="/product"
              class="btn-primary inline-flex items-center gap-2"
            >
              Shop Now
            </RouterLink>
          </div>
        </div>

        <!-- Cart & Checkout -->
        <div v-else>
          <div class="mb-8">
            <RouterLink
              to="/product"
              class="inline-flex items-center gap-2 text-text-muted hover:text-text-main transition-colors"
            >
              <ArrowLeft class="size-4" />
              Continue Shopping
            </RouterLink>
          </div>

          <h1 class="text-4xl md:text-5xl mb-8 text-text-main text-balance">
            {{ step === 'cart' ? 'Shopping Cart' : 'Checkout' }}
          </h1>

          <div class="grid md:grid-cols-3 gap-8">
            <!-- Cart Items / Payment Form -->
            <div class="md:col-span-2">
              <!-- Cart View -->
              <div v-if="step === 'cart'" class="space-y-4">
                <div v-for="item in cartStore.items" :key="item.id" class="card flex gap-6">
                  <div class="size-24 bg-bg-main border border-border-main flex items-center justify-center flex-shrink-0">
                    <span class="text-text-muted text-sm">Image</span>
                  </div>
                  <div class="flex-1">
                    <h3 class="text-xl mb-2 text-text-main">{{ item.name }}</h3>
                    <p class="text-text-muted mb-4 tabular-nums">${{ item.price.toFixed(2) }}</p>
                    <div class="flex items-center gap-4">
                      <button
                        @click="cartStore.updateQuantity(item.id, item.quantity - 1)"
                        class="btn-small text-text-main hover:text-text-muted"
                        aria-label="Decrease quantity"
                      >
                        -
                      </button>
                      <span class="text-text-main tabular-nums">{{ item.quantity }}</span>
                      <button
                        @click="cartStore.updateQuantity(item.id, item.quantity + 1)"
                        class="btn-small text-text-main hover:text-text-muted"
                        aria-label="Increase quantity"
                      >
                        +
                      </button>
                    </div>
                  </div>
                  <div class="flex flex-col items-end justify-between">
                    <button
                      @click="cartStore.removeFromCart(item.id)"
                      class="text-text-muted hover:text-red-500 transition-colors"
                      aria-label="Remove item"
                    >
                      <Trash2 class="size-5" />
                    </button>
                    <p class="text-xl text-text-main tabular-nums">
                      ${{ (item.price * item.quantity).toFixed(2) }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- Payment Form -->
              <form v-else @submit="handlePlaceOrder" class="card">
                <h2 class="text-2xl mb-6 text-text-main flex items-center gap-2">
                  <CreditCard class="size-6" />
                  Payment Information
                </h2>

                <div class="space-y-4">
                  <div>
                    <label class="block text-text-muted mb-2">Email</label>
                    <input
                      type="email"
                      name="email"
                      v-model="formData.email"
                      required
                      class="input"
                      placeholder="your@email.com"
                    />
                  </div>

                  <div>
                    <label class="block text-text-muted mb-2">Full Name</label>
                    <input
                      type="text"
                      name="name"
                      v-model="formData.name"
                      required
                      class="input"
                      placeholder="John Doe"
                    />
                  </div>

                  <div>
                    <label class="block text-text-muted mb-2">Address</label>
                    <input
                      type="text"
                      name="address"
                      v-model="formData.address"
                      required
                      class="input"
                      placeholder="123 Main St"
                    />
                  </div>

                  <div class="grid grid-cols-2 gap-4">
                    <div>
                      <label class="block text-text-muted mb-2">City</label>
                      <input
                        type="text"
                        name="city"
                        v-model="formData.city"
                        required
                        class="input"
                        placeholder="New York"
                      />
                    </div>
                    <div>
                      <label class="block text-text-muted mb-2">ZIP Code</label>
                      <input
                        type="text"
                        name="zipCode"
                        v-model="formData.zipCode"
                        required
                        class="input"
                        placeholder="10001"
                      />
                    </div>
                  </div>

                  <div class="space-y-4">
                    <!-- Stripe Card Element -->
                    <div class="p-4 bg-bg-card border border-border-main rounded-lg">
                      <label class="block text-text-muted mb-2">Card Details</label>
                      <div id="card-element" data-testid="card-element" class="p-3 bg-bg-main border border-border-main rounded-md"></div>
                      <div v-if="stripeError" class="mt-2 text-red-500 text-sm">{{ stripeError }}</div>
                    </div>
                  </div>

                </div>

                <div class="mt-6 p-4 bg-bg-main border border-border-main flex items-center gap-2 text-sm text-text-muted">
                  <Lock class="size-4" />
                  Your payment information is secure and encrypted
                </div>
              </form>
            </div>

            <!-- Order Summary -->
            <div>
              <div class="card sticky top-24">
                <h2 class="text-2xl mb-6 text-text-main">Order Summary</h2>

                <div class="space-y-3 mb-6 pb-6 border-b border-border-main">
                  <div class="flex justify-between text-text-muted">
                    <span>Subtotal</span>
                    <span class="tabular-nums">${{ cartStore.totalPrice.toFixed(2) }}</span>
                  </div>
                  <div class="flex justify-between text-text-muted">
                    <span>Shipping</span>
                    <span class="tabular-nums">${{ shippingCost.toFixed(2) }}</span>
                  </div>
                  <div class="flex justify-between text-text-muted">
                    <span>Tax</span>
                    <span class="tabular-nums">${{ tax.toFixed(2) }}</span>
                  </div>
                </div>

                <div class="flex justify-between text-2xl mb-6 text-text-main">
                  <span>Total</span>
                  <span class="tabular-nums">${{ finalTotal.toFixed(2) }}</span>
                </div>

                <button
                  v-if="step === 'cart'"
                  @click="step = 'payment'"
                  class="btn-primary w-full"
                >
                  Proceed to Checkout
                </button>
                <button
                  v-else
                  type="submit"
                  @click="handlePlaceOrder"
                  class="btn-primary w-full"
                >
                  Place Order
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
