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

// Auth API
export const authApi = {
  login: (email, password) => {
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);
    
    return apiFetch('/auth/login/access-token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formData,
    });
  },

  signup: (userData) => apiFetch('/auth/signup', {
    method: 'POST',
    body: JSON.stringify(userData),
  }),
};

// Users API
export const usersApi = {
  getMe: (token) => apiFetch('/users/me', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  }),
  
  getOrders: (token) => apiFetch('/users/me/orders', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  }),

  updateProfile: (token, userData) => apiFetch('/users/me', {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(userData)
  }),
};

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

// Payment API
export const paymentApi = {
  createIntent: (amount, currency = 'usd') => apiFetch('/payments/create-intent', {
    method: 'POST',
    body: JSON.stringify({ amount, currency }),
  }),
};

// Health Check
export const healthApi = {
  check: () => apiFetch('/health'),
};
