<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import { ShoppingCart, User, LogOut, Sun, Moon } from 'lucide-vue-next'
import { useCartStore } from '../stores/cart'
import { useAuthStore } from '../stores/auth'
import { useThemeStore } from '../stores/theme'

const cartStore = useCartStore()
const authStore = useAuthStore()
const themeStore = useThemeStore()

// Computed property for total items in cart
const totalItems = computed(() => cartStore.totalItems)
</script>

<template>
  <header class="bg-bg-main border-b border-border-main sticky top-0 z-50 transition-colors duration-300">
    <div class="container mx-auto px-4 md:px-6 flex items-center justify-between h-20">
      <!-- Logo (Left) -->
      <RouterLink to="/" class="flex items-center gap-2">
        <div class="size-12 bg-bg-card flex items-center justify-center">
          <span class="text-text-main font-bold text-lg">AXYS</span>
        </div>
      </RouterLink>

      <!-- Navigation (Center - hidden on mobile) -->
      <nav class="hidden md:flex items-center gap-8">
        <RouterLink
          to="/"
          class="text-text-muted hover:text-text-main transition-colors duration-200"
          :class="{ 'text-text-main': $route.path === '/' }"
        >
          Home
        </RouterLink>
        <RouterLink
          to="/product"
          class="text-text-muted hover:text-text-main transition-colors duration-200"
          :class="{ 'text-text-main': $route.path === '/product' }"
        >
          Product
        </RouterLink>
      </nav>

      <!-- Actions (Right) -->
      <div class="flex items-center gap-4">
        <!-- Theme Toggle -->
        <button 
          @click="themeStore.toggleTheme" 
          class="text-text-muted hover:text-text-main transition-colors duration-200 p-1"
          aria-label="Toggle Theme"
        >
          <Sun v-if="themeStore.theme === 'dark'" class="size-5" />
          <Moon v-else class="size-5" />
        </button>

        <!-- Auth Links -->
        <div v-if="authStore.isAuthenticated" class="flex items-center gap-4">
          <RouterLink to="/dashboard" class="flex items-center gap-2 text-text-muted hover:text-text-main transition-colors">
             <User class="size-5" />
             <span class="text-sm hidden sm:block">{{ authStore.user?.full_name || 'My Account' }}</span>
          </RouterLink>
          <button @click="authStore.logout" class="text-text-muted hover:text-text-main transition-colors" aria-label="Logout">
            <LogOut class="size-5" />
          </button>
        </div>
        <RouterLink
          v-else
          to="/login"
          class="text-text-muted hover:text-text-main transition-colors"
          aria-label="Login"
        >
          <User class="size-5" />
        </RouterLink>

        <!-- Shopping Cart -->
        <RouterLink
          to="/checkout"
          class="relative p-2 text-text-muted hover:text-text-main transition-colors duration-200"
          aria-label="View Cart"
        >
          <ShoppingCart class="size-6" />
          <!-- Cart Badge -->
          <span
            v-if="totalItems > 0"
            class="absolute -top-1 -right-1 bg-text-main text-bg-main text-xs font-bold rounded-full size-5 flex items-center justify-center tabular-nums"
          >
            {{ totalItems }}
          </span>
        </RouterLink>
      </div>
    </div>
  </header>
</template>

<style scoped>
/* Additional styles if needed */
</style>
