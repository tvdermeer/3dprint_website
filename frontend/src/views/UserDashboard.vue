<template>
  <div class="min-h-full flex flex-col">
    <div class="container mx-auto px-4 py-8">
      <div class="flex flex-col md:flex-row gap-8">
        <!-- Sidebar -->
        <aside class="w-full md:w-64 flex-shrink-0">
          <div class="bg-bg-card rounded-lg border border-border-main p-6">
            <div class="flex items-center space-x-3 mb-6">
              <div class="h-10 w-10 rounded-full bg-primary-100 flex items-center justify-center text-primary-600 font-bold">
                {{ userInitials }}
              </div>
              <div>
                <p class="font-medium text-text-main">{{ authStore.user?.full_name || 'User' }}</p>
                <p class="text-xs text-text-muted truncate max-w-[120px]">{{ authStore.user?.email }}</p>
              </div>
            </div>
            
            <nav class="space-y-1">
              <button 
                @click="currentTab = 'dashboard'" 
                class="w-full flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors"
                :class="currentTab === 'dashboard' ? 'bg-primary-50 text-primary-600 dark:bg-primary-900/20 dark:text-primary-400' : 'text-text-muted hover:bg-bg-muted hover:text-text-main'"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                </svg>
                Dashboard
              </button>
              
              <button 
                @click="currentTab = 'orders'"
                class="w-full flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors"
                :class="currentTab === 'orders' ? 'bg-primary-50 text-primary-600 dark:bg-primary-900/20 dark:text-primary-400' : 'text-text-muted hover:bg-bg-muted hover:text-text-main'"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
                </svg>
                Orders
              </button>
              
              <button 
                @click="currentTab = 'settings'"
                class="w-full flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors"
                :class="currentTab === 'settings' ? 'bg-primary-50 text-primary-600 dark:bg-primary-900/20 dark:text-primary-400' : 'text-text-muted hover:bg-bg-muted hover:text-text-main'"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                Settings
              </button>
              
              <button 
                @click="handleLogout"
                class="w-full mt-4 flex items-center px-3 py-2 text-sm font-medium text-red-600 rounded-md hover:bg-red-50 dark:hover:bg-red-900/20 transition-colors"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
                Logout
              </button>
            </nav>
          </div>
        </aside>
        
        <!-- Main Content -->
        <div class="flex-grow">
          <div class="bg-bg-card rounded-lg border border-border-main p-8 min-h-[400px]">
            
            <!-- Dashboard Tab -->
            <div v-if="currentTab === 'dashboard'">
              <h1 class="text-2xl font-bold text-text-main mb-4">Dashboard</h1>
              <p class="text-text-muted mb-6">
                Welcome back, <span class="font-semibold text-text-main">{{ authStore.user?.full_name || authStore.user?.email }}</span>!
              </p>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="border border-border-main rounded-lg p-6 bg-bg-muted">
                  <h3 class="font-medium text-text-main mb-2">Account Status</h3>
                  <p class="text-sm text-text-muted">
                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400">
                      Active
                    </span>
                  </p>
                </div>
                
                <div class="border border-border-main rounded-lg p-6 bg-bg-muted">
                  <h3 class="font-medium text-text-main mb-2">Member Since</h3>
                  <p class="text-sm text-text-muted">January 2026</p>
                </div>
              </div>
            </div>

            <!-- Orders Tab -->
            <div v-else-if="currentTab === 'orders'">
              <h1 class="text-2xl font-bold text-text-main mb-6">Order History</h1>
              
              <div v-if="loadingOrders" class="text-center py-12">
                <div class="inline-block animate-spin rounded-full h-8 w-8 border-4 border-primary-500 border-t-transparent"></div>
                <p class="mt-2 text-text-muted">Loading orders...</p>
              </div>
              
              <div v-else-if="orders.length === 0" class="text-center py-12 border border-dashed border-border-main rounded-lg">
                <p class="text-text-muted mb-4">You haven't placed any orders yet.</p>
                <router-link to="/product" class="btn btn-primary gap-2">
                  <ShoppingCart class="size-4" />
                  Start Shopping
                </router-link>
              </div>
              
              <div v-else class="space-y-4">
                <div v-for="order in orders" :key="order.id" class="border border-border-main rounded-lg overflow-hidden">
                  <div class="bg-bg-muted px-4 py-3 flex flex-wrap items-center justify-between gap-4 border-b border-border-main">
                    <div class="flex gap-6">
                      <div>
                        <p class="text-xs text-text-muted uppercase font-bold">Order Placed</p>
                        <p class="text-sm text-text-main">{{ formatDate(order.created_at) }}</p>
                      </div>
                      <div>
                        <p class="text-xs text-text-muted uppercase font-bold">Total</p>
                        <p class="text-sm text-text-main">${{ order.total_amount.toFixed(2) }}</p>
                      </div>
                    </div>
                    <div>
                      <p class="text-xs text-text-muted uppercase font-bold">Order # {{ order.order_number }}</p>
                      <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium capitalize"
                        :class="{
                          'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400': order.status === 'pending',
                          'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400': order.status === 'paid' || order.status === 'delivered',
                          'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400': order.status === 'shipped',
                          'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400': order.status === 'cancelled'
                        }"
                      >
                        {{ order.status }}
                      </span>
                    </div>
                  </div>
                  <div class="p-4">
                    <ul class="divide-y divide-border-main">
                      <li v-for="item in order.items" :key="item.id" class="py-2 flex justify-between items-center">
                        <div class="flex items-center">
                          <span class="font-medium text-text-main">{{ item.quantity }}x</span>
                          <span class="ml-4 text-text-muted">Product #{{ item.product_id }}</span>
                        </div>
                        <span class="text-text-main font-medium">${{ item.price_at_purchase.toFixed(2) }}</span>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Settings Tab -->
            <div v-else-if="currentTab === 'settings'">
              <h1 class="text-2xl font-bold text-text-main mb-6">Settings</h1>
              
              <div class="max-w-md">
                <form @submit.prevent="handleUpdateProfile" class="space-y-6">
                  
                  <!-- Success Message -->
                  <div v-if="updateSuccess" class="p-4 bg-green-500/10 border border-green-500/20 rounded-lg flex items-center gap-3 text-green-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>
                    <p class="text-sm">Profile updated successfully!</p>
                  </div>
                  
                  <!-- Error Message -->
                  <div v-if="updateError" class="p-4 bg-red-500/10 border border-red-500/20 rounded-lg flex items-center gap-3 text-red-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    <p class="text-sm">{{ updateError }}</p>
                  </div>

                  <div>
                    <label class="block text-text-muted mb-2">Email</label>
                    <input
                      type="email"
                      :value="authStore.user?.email"
                      disabled
                      class="input bg-bg-muted cursor-not-allowed opacity-75"
                    />
                    <p class="mt-1 text-xs text-text-muted">Email cannot be changed.</p>
                  </div>

                  <div>
                    <label class="block text-text-muted mb-2">Full Name</label>
                    <input
                      type="text"
                      v-model="settingsForm.full_name"
                      class="input"
                    />
                  </div>

                  <div class="pt-4 border-t border-border-main">
                    <h3 class="text-lg font-medium text-text-main mb-4">Change Password</h3>
                    <p class="text-sm text-text-muted mb-4">Leave blank to keep current password.</p>
                    
                    <div class="space-y-4">
                      <div>
                        <label class="block text-text-muted mb-2">New Password</label>
                        <input
                          type="password"
                          v-model="settingsForm.password"
                          class="input"
                          placeholder="••••••••"
                        />
                      </div>
                      
                      <div>
                        <label class="block text-text-muted mb-2">Confirm Password</label>
                        <input
                          type="password"
                          v-model="settingsForm.confirmPassword"
                          class="input"
                          placeholder="••••••••"
                        />
                      </div>
                    </div>
                  </div>

                  <div class="pt-4">
                    <button
                      type="submit"
                      :disabled="authStore.loading"
                      class="btn btn-primary w-full md:w-auto gap-2"
                    >
                      <span v-if="authStore.loading" class="size-4 border-2 border-bg-main/20 border-t-bg-main rounded-full animate-spin"></span>
                      <Save v-else class="size-4" />
                      Save Changes
                    </button>
                  </div>
                </form>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { usersApi } from '../api/client'
import { ShoppingCart, Save } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()
const currentTab = ref('dashboard')
const orders = ref([])
const loadingOrders = ref(false)

// Settings Form State
const settingsForm = ref({
  full_name: authStore.user?.full_name || '',
  password: '',
  confirmPassword: ''
})
const updateSuccess = ref(false)
const updateError = ref('')

const userInitials = computed(() => {
  const name = authStore.user?.full_name || authStore.user?.email || 'User'
  return name.substring(0, 2).toUpperCase()
})

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const fetchOrders = async () => {
  loadingOrders.value = true
  try {
    const data = await usersApi.getOrders(authStore.token)
    orders.value = data
  } catch (err) {
    console.error('Failed to fetch orders:', err)
  } finally {
    loadingOrders.value = false
  }
}

const handleUpdateProfile = async () => {
  updateError.value = ''
  updateSuccess.value = false
  
  if (settingsForm.value.password && settingsForm.value.password !== settingsForm.value.confirmPassword) {
    updateError.value = "Passwords do not match"
    return
  }
  
  const payload = {
    full_name: settingsForm.value.full_name,
    email: authStore.user?.email // Required by schema
  }
  
  if (settingsForm.value.password) {
    payload.password = settingsForm.value.password
  }
  
  const success = await authStore.updateProfile(payload)
  
  if (success) {
    updateSuccess.value = true
    settingsForm.value.password = ''
    settingsForm.value.confirmPassword = ''
  } else {
    updateError.value = authStore.error || 'Failed to update profile'
  }
}

// Watch for tab changes to fetch data
watch(currentTab, (newTab) => {
  if (newTab === 'orders' && orders.value.length === 0) {
    fetchOrders()
  }
  // Reset form when entering settings
  if (newTab === 'settings' && authStore.user) {
    settingsForm.value.full_name = authStore.user.full_name || ''
    settingsForm.value.password = ''
    settingsForm.value.confirmPassword = ''
    updateSuccess.value = false
    updateError.value = ''
  }
})
</script>