import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  // State
  const items = ref([])

  // Load from localStorage on init
  const loadFromLocalStorage = () => {
    try {
      const stored = localStorage.getItem('axys-cart')
      if (stored) {
        items.value = JSON.parse(stored)
      }
    } catch (error) {
      console.error('Failed to load cart from localStorage:', error)
    }
  }

  // Save to localStorage
  const saveToLocalStorage = () => {
    try {
      localStorage.setItem('axys-cart', JSON.stringify(items.value))
    } catch (error) {
      console.error('Failed to save cart to localStorage:', error)
    }
  }

  // Getters
  const totalItems = computed(() => {
    return items.value.reduce((sum, item) => sum + item.quantity, 0)
  })

  const totalPrice = computed(() => {
    return items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  })

  const cartItems = computed(() => items.value)

  // Actions
  const addToCart = (item, quantity = 1) => {
    const existingItem = items.value.find((i) => i.id === item.id)

    if (existingItem) {
      // Item already in cart, increment quantity
      existingItem.quantity += quantity
    } else {
      // New item, add to cart with quantity
      items.value.push({
        ...item,
        quantity: quantity,
      })
    }

    saveToLocalStorage()
  }

  const removeFromCart = (itemId) => {
    items.value = items.value.filter((item) => item.id !== itemId)
    saveToLocalStorage()
  }

  const updateQuantity = (itemId, quantity) => {
    if (quantity <= 0) {
      removeFromCart(itemId)
      return
    }

    const item = items.value.find((i) => i.id === itemId)
    if (item) {
      item.quantity = quantity
      saveToLocalStorage()
    }
  }

  const clearCart = () => {
    items.value = []
    saveToLocalStorage()
  }

  // Initialize cart from localStorage
  loadFromLocalStorage()

  return {
    // State
    items,

    // Getters
    totalItems,
    totalPrice,
    cartItems,

    // Actions
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    loadFromLocalStorage,
    saveToLocalStorage,
  }
})
