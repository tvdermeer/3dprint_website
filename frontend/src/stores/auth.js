import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '../api/client'

export const useAuthStore = defineStore('auth', () => {
  // State
  const token = ref(localStorage.getItem('axys-token') || null)
  const user = ref(JSON.parse(localStorage.getItem('axys-user') || 'null'))
  const loading = ref(false)
  const error = ref(null)

  // Getters
  const isAuthenticated = computed(() => !!token.value)

  // Actions
  const login = async (email, password) => {
    loading.value = true
    error.value = null
    try {
      const data = await authApi.login(email, password)
      
      // Save token
      token.value = data.access_token
      localStorage.setItem('axys-token', data.access_token)
      
      // In a real app, we might fetch user profile here
      // For now, we'll simulate a user object
      const userData = { email }
      user.value = userData
      localStorage.setItem('axys-user', JSON.stringify(userData))
      
      return true
    } catch (err) {
      console.error('Login failed:', err)
      error.value = err.message || 'Login failed'
      return false
    } finally {
      loading.value = false
    }
  }

  const signup = async (userData) => {
    loading.value = true
    error.value = null
    try {
      await authApi.signup(userData)
      // Auto login after signup? Or require manual login?
      // For now, require manual login
      return true
    } catch (err) {
      console.error('Signup failed:', err)
      error.value = err.message || 'Signup failed'
      return false
    } finally {
      loading.value = false
    }
  }

  const logout = () => {
    token.value = null
    user.value = null
    localStorage.removeItem('axys-token')
    localStorage.removeItem('axys-user')
  }

  return {
    // State
    token,
    user,
    loading,
    error,
    
    // Getters
    isAuthenticated,
    
    // Actions
    login,
    signup,
    logout
  }
})
