<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { Trash2, ArrowLeft, CreditCard, Lock } from 'lucide-vue-next'
import { useCartStore } from '../stores/cart'

import { computed } from 'vue'

const cartStore = useCartStore()
const step = ref('cart') // 'cart', 'payment', 'success'
const formData = ref({
  email: '',
  name: '',
  address: '',
  city: '',
  zipCode: '',
  cardNumber: '',
  expiryDate: '',
  cvv: '',
})

const shippingCost = 9.99
const taxRate = 0.08

const tax = computed(() => cartStore.totalPrice * taxRate)
const finalTotal = computed(() => cartStore.totalPrice + shippingCost + tax.value)

const handleInputChange = (e) => {
  const { name, value } = e.target
  formData.value[name] = value
}

import { ordersApi } from '../api/client'

const handlePlaceOrder = async (e) => {
  e.preventDefault()
  
  try {
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
    
  } catch (error) {
    console.error('Failed to place order:', error)
    alert('Failed to place order. Please try again.')
  }
}
</script>

<template>
  <div class="min-h-screen py-16 bg-dark-900">
    <div class="container mx-auto">
      <div class="max-w-6xl mx-auto">
        <!-- Success Screen -->
        <div v-if="step === 'success'" class="max-w-2xl mx-auto">
          <div class="card text-center">
            <div class="w-16 h-16 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h1 class="text-4xl mb-4 text-white">Order Confirmed!</h1>
            <p class="text-xl text-gray-400 mb-8">
              Thank you for your purchase. Your order has been successfully placed.
            </p>
            <p class="text-gray-500 mb-8">
              You will receive a confirmation email shortly with tracking information.
            </p>
            <RouterLink
              to="/"
              class="btn-primary inline-flex items-center gap-2"
            >
              <ArrowLeft class="w-5 h-5" />
              Back to Home
            </RouterLink>
          </div>
        </div>

        <!-- Empty Cart -->
        <div v-else-if="cartStore.items.length === 0" class="max-w-2xl mx-auto">
          <div class="card text-center">
            <h1 class="text-4xl mb-4 text-white">Your Cart is Empty</h1>
            <p class="text-xl text-gray-400 mb-8">
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
              class="inline-flex items-center gap-2 text-gray-400 hover:text-white transition-colors"
            >
              <ArrowLeft class="w-4 h-4" />
              Continue Shopping
            </RouterLink>
          </div>

          <h1 class="text-4xl md:text-5xl mb-8 text-white">
            {{ step === 'cart' ? 'Shopping Cart' : 'Checkout' }}
          </h1>

          <div class="grid md:grid-cols-3 gap-8">
            <!-- Cart Items / Payment Form -->
            <div class="md:col-span-2">
              <!-- Cart View -->
              <div v-if="step === 'cart'" class="space-y-4">
                <div v-for="item in cartStore.items" :key="item.id" class="card flex gap-6">
                  <div class="w-24 h-24 bg-dark-900 border border-dark-700 flex items-center justify-center flex-shrink-0">
                    <span class="text-gray-400 text-sm">Image</span>
                  </div>
                  <div class="flex-1">
                    <h3 class="text-xl mb-2 text-white">{{ item.name }}</h3>
                    <p class="text-gray-400 mb-4">${{ item.price.toFixed(2) }}</p>
                    <div class="flex items-center gap-4">
                      <button
                        @click="cartStore.updateQuantity(item.id, item.quantity - 1)"
                        class="btn-small"
                      >
                        -
                      </button>
                      <span class="text-white">{{ item.quantity }}</span>
                      <button
                        @click="cartStore.updateQuantity(item.id, item.quantity + 1)"
                        class="btn-small"
                      >
                        +
                      </button>
                    </div>
                  </div>
                  <div class="flex flex-col items-end justify-between">
                    <button
                      @click="cartStore.removeFromCart(item.id)"
                      class="text-gray-400 hover:text-red-500 transition-colors"
                    >
                      <Trash2 class="w-5 h-5" />
                    </button>
                    <p class="text-xl text-white">
                      ${{ (item.price * item.quantity).toFixed(2) }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- Payment Form -->
              <form v-else @submit="handlePlaceOrder" class="card">
                <h2 class="text-2xl mb-6 text-white flex items-center gap-2">
                  <CreditCard class="w-6 h-6" />
                  Payment Information
                </h2>

                <div class="space-y-4">
                  <div>
                    <label class="block text-gray-400 mb-2">Email</label>
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
                    <label class="block text-gray-400 mb-2">Full Name</label>
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
                    <label class="block text-gray-400 mb-2">Address</label>
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
                      <label class="block text-gray-400 mb-2">City</label>
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
                      <label class="block text-gray-400 mb-2">ZIP Code</label>
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

                  <div>
                    <label class="block text-gray-400 mb-2">Card Number</label>
                    <input
                      type="text"
                      name="cardNumber"
                      v-model="formData.cardNumber"
                      required
                      maxlength="16"
                      class="input"
                      placeholder="1234 5678 9012 3456"
                    />
                  </div>

                  <div class="grid grid-cols-2 gap-4">
                    <div>
                      <label class="block text-gray-400 mb-2">Expiry Date</label>
                      <input
                        type="text"
                        name="expiryDate"
                        v-model="formData.expiryDate"
                        required
                        class="input"
                        placeholder="MM/YY"
                      />
                    </div>
                    <div>
                      <label class="block text-gray-400 mb-2">CVV</label>
                      <input
                        type="text"
                        name="cvv"
                        v-model="formData.cvv"
                        required
                        maxlength="3"
                        class="input"
                        placeholder="123"
                      />
                    </div>
                  </div>
                </div>

                <div class="mt-6 p-4 bg-dark-900 border border-dark-700 flex items-center gap-2 text-sm text-gray-400">
                  <Lock class="w-4 h-4" />
                  Your payment information is secure and encrypted
                </div>
              </form>
            </div>

            <!-- Order Summary -->
            <div>
              <div class="card sticky top-24">
                <h2 class="text-2xl mb-6 text-white">Order Summary</h2>

                <div class="space-y-3 mb-6 pb-6 border-b border-dark-700">
                  <div class="flex justify-between text-gray-400">
                    <span>Subtotal</span>
                    <span>${{ cartStore.totalPrice.toFixed(2) }}</span>
                  </div>
                  <div class="flex justify-between text-gray-400">
                    <span>Shipping</span>
                    <span>${{ shippingCost.toFixed(2) }}</span>
                  </div>
                  <div class="flex justify-between text-gray-400">
                    <span>Tax</span>
                    <span>${{ tax.toFixed(2) }}</span>
                  </div>
                </div>

                <div class="flex justify-between text-2xl mb-6 text-white">
                  <span>Total</span>
                  <span>${{ finalTotal.toFixed(2) }}</span>
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
