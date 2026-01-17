import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi, usersApi } from '../api/client'

export const useAuthStore = defineStore('auth', () => {
  // State
  const token = ref(localStorage.getItem('axys-token') || null)
  const user = ref(JSON.parse(localStorage.getItem('axys-user') || 'null'))
  const loading = ref(false)
  const error = ref(null)

  // Getters
  const isAuthenticated = computed(() => !!token.value)

  // Actions
  const fetchUser = async () => {
    if (!token.value) return null
    
    try {
      const userData = await usersApi.getMe(token.value)
      user.value = userData
      localStorage.setItem('axys-user', JSON.stringify(userData))
      return userData
    } catch (err) {
      console.error('Failed to fetch user profile:', err)
      // If 401, clear session
      if (err.message.includes('401') || err.message.includes('Unauthorized')) {
        logout()
      }
      return null
    }
  }

  const updateProfile = async (userData) => {
    loading.value = true
    error.value = null
    try {
      const updatedUser = await usersApi.updateProfile(token.value, userData)
      user.value = updatedUser
      localStorage.setItem('axys-user', JSON.stringify(updatedUser))
      return true
    } catch (err) {
      console.error('Update failed:', err)
      error.value = err.message || 'Update failed'
      return false
    } finally {
      loading.value = false
    }
  }

  const login = async (email, password) => {
    loading.value = true
    error.value = null
    try {
      const data = await authApi.login(email, password)
      
      // Save token
      token.value = data.access_token
      localStorage.setItem('axys-token', data.access_token)
      
      // Fetch user profile
      await fetchUser()
      
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

  const recoverPassword = async (email) => {
    loading.value = true
    error.value = null
    try {
      await authApi.recoverPassword(email)
      return true
    } catch (err) {
      console.error('Password recovery failed:', err)
      error.value = err.message || 'Password recovery failed'
      return false
    } finally {
      loading.value = false
    }
  }

  const resetPassword = async (token, newPassword) => {
    loading.value = true
    error.value = null
    try {
      await authApi.resetPassword(token, newPassword)
      return true
    } catch (err) {
      console.error('Password reset failed:', err)
      error.value = err.message || 'Password reset failed'
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
    logout,
    fetchUser,
    updateProfile,
    recoverPassword,
    resetPassword
  }
})
