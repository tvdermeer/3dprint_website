<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { Lock, Mail, User, AlertCircle } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()

const isLogin = ref(true) // Toggle between login and signup
const formData = ref({
  email: '',
  password: '',
  full_name: ''
})

const handleSubmit = async () => {
  if (isLogin.value) {
    const success = await authStore.login(formData.value.email, formData.value.password)
    if (success) {
      router.push('/')
    }
  } else {
    // Signup
    const success = await authStore.signup({
      email: formData.value.email,
      password: formData.value.password,
      full_name: formData.value.full_name
    })
    
    if (success) {
      // Switch to login mode and show success message (could be improved)
      isLogin.value = true
      alert('Account created! Please log in.')
      formData.value.password = '' // Clear password
    }
  }
}
</script>

<template>
  <div class="min-h-screen py-16 bg-dark-900 flex items-center justify-center">
    <div class="container mx-auto px-4">
      <div class="max-w-md mx-auto card">
        <h1 class="text-3xl mb-6 text-white text-center">
          {{ isLogin ? 'Welcome Back' : 'Create Account' }}
        </h1>

        <!-- Error Alert -->
        <div v-if="authStore.error" class="mb-6 p-4 bg-red-500/10 border border-red-500/20 rounded-lg flex items-center gap-3 text-red-400">
          <AlertCircle class="w-5 h-5 flex-shrink-0" />
          <p class="text-sm">{{ authStore.error }}</p>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-4">
          
          <!-- Full Name (Signup only) -->
          <div v-if="!isLogin">
            <label class="block text-gray-400 mb-2">Full Name</label>
            <div class="relative">
              <User class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500" />
              <input
                type="text"
                v-model="formData.full_name"
                required
                class="input pl-10"
                placeholder="John Doe"
              />
            </div>
          </div>

          <!-- Email -->
          <div>
            <label class="block text-gray-400 mb-2">Email</label>
            <div class="relative">
              <Mail class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500" />
              <input
                type="email"
                v-model="formData.email"
                required
                class="input pl-10"
                placeholder="your@email.com"
              />
            </div>
          </div>

          <!-- Password -->
          <div>
            <label class="block text-gray-400 mb-2">Password</label>
            <div class="relative">
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500" />
              <input
                type="password"
                v-model="formData.password"
                required
                class="input pl-10"
                placeholder="••••••••"
              />
            </div>
          </div>

          <button
            type="submit"
            :disabled="authStore.loading"
            class="btn-primary w-full flex items-center justify-center gap-2"
          >
            <span v-if="authStore.loading" class="w-4 h-4 border-2 border-white/20 border-t-white rounded-full animate-spin"></span>
            {{ isLogin ? 'Log In' : 'Sign Up' }}
          </button>
        </form>

        <div class="mt-6 text-center text-gray-400 text-sm">
          <p v-if="isLogin">
            Don't have an account? 
            <button @click="isLogin = false; authStore.error = null" class="text-white hover:underline">Sign up</button>
          </p>
          <p v-else>
            Already have an account? 
            <button @click="isLogin = true; authStore.error = null" class="text-white hover:underline">Log in</button>
          </p>
        </div>

      </div>
    </div>
  </div>
</template>
