<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { Lock, AlertCircle, CheckCircle } from 'lucide-vue-next'
import { validatePassword } from '../utils/validation'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const token = ref('')
const password = ref('')
const confirmPassword = ref('')
const passwordError = ref('')
const successMessage = ref('')

onMounted(() => {
  token.value = route.query.token
  if (!token.value) {
    authStore.error = 'Invalid or missing reset token.'
  }
})

const handlePasswordInput = () => {
  const { isValid, error } = validatePassword(password.value)
  passwordError.value = isValid ? '' : error
}

const handleSubmit = async () => {
  if (passwordError.value) return
  if (password.value !== confirmPassword.value) {
    authStore.error = 'Passwords do not match'
    return
  }

  const success = await authStore.resetPassword(token.value, password.value)
  
  if (success) {
    successMessage.value = 'Password reset successfully! Redirecting to login...'
    setTimeout(() => {
      router.push('/auth')
    }, 2000)
  }
}
</script>

<template>
  <div class="min-h-dvh py-16 bg-bg-main flex items-center justify-center transition-colors duration-300">
    <div class="container mx-auto px-4">
      <div class="max-w-md mx-auto card">
        <h1 class="text-3xl mb-6 text-text-main text-center text-balance">
          Reset Password
        </h1>

        <!-- Error Alert -->
        <div v-if="authStore.error" class="mb-6 p-4 bg-red-500/10 border border-red-500/20 rounded-lg flex items-center gap-3 text-red-400">
          <AlertCircle class="size-5 flex-shrink-0" />
          <p class="text-sm">{{ authStore.error }}</p>
        </div>

        <!-- Success Alert -->
        <div v-if="successMessage" class="mb-6 p-4 bg-green-500/10 border border-green-500/20 rounded-lg flex items-center gap-3 text-green-400">
          <CheckCircle class="size-5 flex-shrink-0" />
          <p class="text-sm">{{ successMessage }}</p>
        </div>

        <form v-if="!successMessage && token" @submit.prevent="handleSubmit" class="space-y-4">
          
          <!-- New Password -->
          <div>
            <label class="block text-text-muted mb-2">New Password</label>
            <div class="relative">
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 size-5 text-text-muted" />
              <input
                type="password"
                v-model="password"
                required
                @input="handlePasswordInput"
                class="input pl-10 transition-colors"
                :class="{ 'border-red-500 focus:border-red-500 focus:ring-red-500/20': passwordError }"
                placeholder="New Password"
              />
            </div>
            <p v-if="passwordError" class="mt-1 text-sm text-red-500">{{ passwordError }}</p>
          </div>

          <!-- Confirm Password -->
          <div>
            <label class="block text-text-muted mb-2">Confirm Password</label>
            <div class="relative">
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 size-5 text-text-muted" />
              <input
                type="password"
                v-model="confirmPassword"
                required
                class="input pl-10"
                placeholder="Confirm Password"
              />
            </div>
          </div>

          <button
            type="submit"
            :disabled="authStore.loading"
            class="btn-primary w-full flex items-center justify-center gap-2"
          >
            <span v-if="authStore.loading" class="size-4 border-2 border-bg-main/20 border-t-bg-main rounded-full animate-spin"></span>
            Reset Password
          </button>
        </form>
        
        <div v-if="!token" class="text-center">
            <button @click="router.push('/auth')" class="text-text-main hover:underline">Back to Login</button>
        </div>

      </div>
    </div>
  </div>
</template>
