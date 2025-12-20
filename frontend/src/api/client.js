const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

/**
 * Generic fetch wrapper with error handling
 */
async function apiFetch(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;
  const defaultHeaders = {
    'Content-Type': 'application/json',
  };

  const config = {
    ...options,
    headers: {
      ...defaultHeaders,
      ...options.headers,
    },
  };

  try {
    const response = await fetch(url, config);
    
    // Parse JSON if possible
    let data;
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      data = await response.json();
    } else {
      data = await response.text();
    }

    if (!response.ok) {
      throw new Error(data.message || data.detail || 'API request failed');
    }

    return data;
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error);
    throw error;
  }
}

// Products API
export const productsApi = {
  getAll: (params) => {
    const queryString = new URLSearchParams(params).toString();
    return apiFetch(`/products?${queryString}`);
  },
  
  getById: (id) => apiFetch(`/products/${id}`),
  
  checkStock: (id, quantity) => apiFetch(`/products/${id}/check-stock`, {
    method: 'POST',
    body: JSON.stringify({ quantity })
  }),
};

// Orders API
export const ordersApi = {
  create: (orderData) => apiFetch('/orders', {
    method: 'POST',
    body: JSON.stringify(orderData),
  }),
  
  getById: (id) => apiFetch(`/orders/${id}`),
  
  getByNumber: (orderNumber) => apiFetch(`/orders/number/${orderNumber}`),
};

// Health Check
export const healthApi = {
  check: () => apiFetch('/health'),
};
