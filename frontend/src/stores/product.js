import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { productsApi } from '../api/client'

export const useProductStore = defineStore('product', () => {
  // State
  const products = ref([])
  const currentProduct = ref(null)
  const loading = ref(false)
  const error = ref(null)

  // Getters
  const featuredProduct = computed(() => {
    // For now, just return the first product or a default fallback
    return products.value[0] || null
  })

  // Actions
  const fetchProducts = async () => {
    loading.value = true
    error.value = null
    try {
      const data = await productsApi.getAll({ limit: 10 })
      // The API returns a paginated response: { items: [], total: 0, ... }
      products.value = data.items || []
    } catch (err) {
      console.error('Failed to fetch products:', err)
      error.value = 'Failed to load products. Please try again later.'
    } finally {
      loading.value = false
    }
  }

  const fetchProductById = async (id) => {
    loading.value = true
    error.value = null
    try {
      const data = await productsApi.getById(id)
      currentProduct.value = data
      return data
    } catch (err) {
      console.error(`Failed to fetch product ${id}:`, err)
      error.value = 'Failed to load product details.'
      return null
    } finally {
      loading.value = false
    }
  }

  return {
    // State
    products,
    currentProduct,
    loading,
    error,
    
    // Getters
    featuredProduct,
    
    // Actions
    fetchProducts,
    fetchProductById
  }
})
