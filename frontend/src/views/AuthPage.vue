<script setup>
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { Lock, Mail, User, AlertCircle, CheckCircle } from 'lucide-vue-next'
import { validatePassword } from '../utils/validation'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const mode = ref('login') // 'login' | 'signup' | 'recover'
const successMessage = ref('')
const formData = ref({
  email: '',
  password: '',
  full_name: ''
})
const passwordError = ref('')

// Clear errors when switching modes
watch(mode, () => {
  authStore.error = null
  successMessage.value = ''
  passwordError.value = ''
})

const handlePasswordInput = () => {
  if (mode.value === 'signup') {
    const { isValid, error } = validatePassword(formData.value.password)
    passwordError.value = isValid ? '' : error
  } else {
    passwordError.value = ''
  }
}

const handleSubmit = async () => {
  successMessage.value = ''
  if (mode.value === 'login') {
    const success = await authStore.login(formData.value.email, formData.value.password)
    if (success) {
      const redirectPath = route.query.redirect || '/dashboard'
      router.push(redirectPath)
    }
  } else if (mode.value === 'signup') {
    if (passwordError.value) return // Block submission if password invalid
    
    const success = await authStore.signup({
      email: formData.value.email,
      password: formData.value.password,
      full_name: formData.value.full_name
    })
    
    if (success) {
      mode.value = 'login'
      successMessage.value = 'Account created! Please log in.'
      formData.value.password = '' 
    }
  } else if (mode.value === 'recover') {
    const success = await authStore.recoverPassword(formData.value.email)
    if (success) {
      successMessage.value = 'If an account exists, a recovery email has been sent.'
      formData.value.email = ''
    }
  }
}
</script>

<template>
  <div class="min-h-dvh py-16 bg-bg-main flex items-center justify-center transition-colors duration-300">
    <div class="container mx-auto px-4">
      <div class="max-w-md mx-auto card">
        <h1 class="text-3xl mb-6 text-text-main text-center text-balance">
          {{ mode === 'login' ? 'Welcome Back' : mode === 'signup' ? 'Create Account' : 'Reset Password' }}
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

        <form @submit.prevent="handleSubmit" class="space-y-4">
          
          <!-- Full Name (Signup only) -->
          <div v-if="mode === 'signup'">
            <label class="block text-text-muted mb-2">Full Name</label>
            <div class="relative">
              <User class="absolute left-3 top-1/2 -translate-y-1/2 size-5 text-text-muted" />
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
            <label class="block text-text-muted mb-2">Email</label>
            <div class="relative">
              <Mail class="absolute left-3 top-1/2 -translate-y-1/2 size-5 text-text-muted" />
              <input
                type="email"
                v-model="formData.email"
                required
                class="input pl-10"
                placeholder="your@email.com"
              />
            </div>
          </div>

          <!-- Password (Login and Signup only) -->
          <div v-if="mode !== 'recover'">
            <label class="block text-text-muted mb-2">Password</label>
            <div class="relative">
              <Lock class="absolute left-3 top-1/2 -translate-y-1/2 size-5 text-text-muted" />
              <input
                type="password"
                v-model="formData.password"
                required
                @input="handlePasswordInput"
                class="input pl-10 transition-colors"
                :class="{ 'border-red-500 focus:border-red-500 focus:ring-red-500/20': passwordError }"
                placeholder="••••••••"
              />
            </div>
            <p v-if="passwordError" class="mt-1 text-sm text-red-500">{{ passwordError }}</p>
          </div>

          <button
            type="submit"
            :disabled="authStore.loading"
            class="btn-primary w-full flex items-center justify-center gap-2"
          >
            <span v-if="authStore.loading" class="size-4 border-2 border-bg-main/20 border-t-bg-main rounded-full animate-spin"></span>
            {{ mode === 'login' ? 'Log In' : mode === 'signup' ? 'Sign Up' : 'Send Reset Link' }}
          </button>
        </form>

        <div class="mt-6 text-center text-text-muted text-sm space-y-2">
          <div v-if="mode === 'login'">
            <button @click="mode = 'recover'" class="text-text-muted hover:text-text-main hover:underline block mx-auto mb-4">
              Forgot your password?
            </button>
            <p>
              Don't have an account? 
              <button @click="mode = 'signup'" class="text-text-main hover:underline">Sign up</button>
            </p>
          </div>
          
          <div v-if="mode === 'signup'">
            <p>
              Already have an account? 
              <button @click="mode = 'login'" class="text-text-main hover:underline">Log in</button>
            </p>
          </div>

          <div v-if="mode === 'recover'">
            <button @click="mode = 'login'" class="text-text-main hover:underline">Back to Login</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>
