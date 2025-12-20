<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { Star, ShoppingCart, Package, Shield, Truck, Check, Loader2 } from 'lucide-vue-next'
import { useCartStore } from '../stores/cart'
import { useProductStore } from '../stores/product'

const cartStore = useCartStore()
const productStore = useProductStore()
const router = useRouter()

const quantity = ref(1)

// Fetch product on mount
onMounted(async () => {
  await productStore.fetchProducts()
})

const product = computed(() => {
  // Use the first product from the store, or a fallback placeholder if loading/empty
  return productStore.featuredProduct || {
    id: 'placeholder',
    name: 'Loading Product...',
    price: 0,
    description: 'Loading...',
    stock: 0
  }
})

const handleAddToCart = () => {
  if (!product.value || product.value.id === 'placeholder') return
  
  cartStore.addToCart(product.value, quantity.value)
  // Navigate to checkout
  router.push('/checkout')
}

</script>

<template>
  <div class="min-h-screen py-16 bg-dark-900">
    <div class="container mx-auto">
      <div class="grid md:grid-cols-2 gap-12 mb-16">
        <!-- Product Image -->
        <div class="bg-gradient-to-br from-dark-800 to-dark-900 p-12 flex items-center justify-center border border-dark-700 h-96">
          <div class="text-center">
            <span class="text-gray-400">Product Image</span>
            <p class="text-sm text-gray-500 mt-2">(To be added in Phase 4)</p>
          </div>
        </div>

        <!-- Product Info -->
        <div class="flex flex-col justify-center">
          <div class="flex items-center gap-2 mb-4">
            <div class="flex gap-1">
              <Star v-for="i in 5" :key="i" class="w-5 h-5 fill-white text-white" />
            </div>
            <span class="text-gray-400 ml-2">(247 reviews)</span>
          </div>

          <h1 class="text-4xl md:text-5xl mb-4 text-white">
            {{ product.name }}
          </h1>

          <div class="text-3xl mb-6 text-white">
            ${{ product.price.toFixed(2) }}
          </div>

          <p class="text-xl text-gray-400 mb-8">
            The ultimate golf club cleaning solution in a premium, durable container. 
            Designed to attach directly to your golf cart for convenient access throughout your round.
          </p>

          <!-- Features List -->
          <div class="space-y-3 mb-8">
            <div class="flex items-center gap-3 text-gray-300">
              <Check class="w-5 h-5 text-white" />
              <span>Premium cleaning formula</span>
            </div>
            <div class="flex items-center gap-3 text-gray-300">
              <Check class="w-5 h-5 text-white" />
              <span>Durable metallic construction</span>
            </div>
            <div class="flex items-center gap-3 text-gray-300">
              <Check class="w-5 h-5 text-white" />
              <span>Universal cart mount included</span>
            </div>
            <div class="flex items-center gap-3 text-gray-300">
              <Check class="w-5 h-5 text-white" />
              <span>Weather-resistant design</span>
            </div>
          </div>

          <!-- Quantity Selector -->
          <div class="mb-6">
            <label class="block text-gray-400 mb-2">Quantity</label>
            <div class="flex items-center gap-4">
              <button
                @click="quantity = Math.max(1, quantity - 1)"
                class="btn-small"
              >
                -
              </button>
              <span class="text-xl text-white min-w-[2rem] text-center">{{ quantity }}</span>
              <button
                @click="quantity = quantity + 1"
                class="btn-small"
              >
                +
              </button>
            </div>
          </div>

          <!-- Add to Cart Button -->
          <button
            @click="handleAddToCart"
            class="btn-primary w-full flex items-center justify-center gap-2 mb-4"
          >
            <ShoppingCart class="w-5 h-5" />
            Add to Cart - ${{ (product.price * quantity).toFixed(2) }}
          </button>

          <!-- Trust Badges -->
          <div class="grid grid-cols-3 gap-4 pt-8 border-t border-dark-700">
            <div class="text-center">
              <Truck class="w-6 h-6 mx-auto mb-2 text-gray-400" />
              <p class="text-sm text-gray-500">Free Shipping</p>
            </div>
            <div class="text-center">
              <Shield class="w-6 h-6 mx-auto mb-2 text-gray-400" />
              <p class="text-sm text-gray-500">1 Year Warranty</p>
            </div>
            <div class="text-center">
              <Package class="w-6 h-6 mx-auto mb-2 text-gray-400" />
              <p class="text-sm text-gray-500">Ships in 24h</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Specifications -->
      <div class="card">
        <h2 class="text-3xl mb-6 text-white">Specifications</h2>
        <div class="grid md:grid-cols-2 gap-6">
          <div>
            <h3 class="text-gray-400 mb-2">Dimensions</h3>
            <p class="text-white">4.5" H × 3.2" W</p>
          </div>
          <div>
            <h3 class="text-gray-400 mb-2">Material</h3>
            <p class="text-white">Powder-coated aluminum</p>
          </div>
          <div>
            <h3 class="text-gray-400 mb-2">Capacity</h3>
            <p class="text-white">12 oz cleaning solution</p>
          </div>
          <div>
            <h3 class="text-gray-400 mb-2">Mounting</h3>
            <p class="text-white">Universal cart bracket</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
