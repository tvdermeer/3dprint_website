<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import { ShoppingCart } from 'lucide-vue-next'
import { useCartStore } from '../stores/cart'

const cartStore = useCartStore()

// Computed property for total items in cart
const totalItems = computed(() => cartStore.totalItems)
</script>

<template>
  <header class="bg-dark-900 border-b border-dark-700 sticky top-0 z-50">
    <div class="container flex items-center justify-between h-20">
      <!-- Logo (Left) -->
      <RouterLink to="/" class="flex items-center gap-2">
        <div class="w-12 h-12 bg-gradient-to-br from-white/30 to-white/10 flex items-center justify-center">
          <span class="text-white font-bold text-lg">AXYS</span>
        </div>
      </RouterLink>

      <!-- Navigation (Center - hidden on mobile) -->
      <nav class="hidden md:flex items-center gap-8">
        <RouterLink
          to="/"
          class="text-gray-400 hover:text-white transition-colors duration-200"
          :class="{ 'text-white': $route.path === '/' }"
        >
          Home
        </RouterLink>
        <RouterLink
          to="/product"
          class="text-gray-400 hover:text-white transition-colors duration-200"
          :class="{ 'text-white': $route.path === '/product' }"
        >
          Product
        </RouterLink>
      </nav>

      <!-- Shopping Cart (Right) -->
      <RouterLink
        to="/checkout"
        class="relative p-2 text-gray-400 hover:text-white transition-colors duration-200"
      >
        <ShoppingCart class="w-6 h-6" />
        <!-- Cart Badge -->
        <span
          v-if="totalItems > 0"
          class="absolute -top-1 -right-1 bg-white text-dark-900 text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center"
        >
          {{ totalItems }}
        </span>
      </RouterLink>
    </div>
  </header>
</template>

<style scoped>
/* Additional styles if needed */
</style>
