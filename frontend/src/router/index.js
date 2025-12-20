import { createRouter, createWebHistory } from 'vue-router'

// Lazy load views for code splitting
const LandingPage = () => import('../views/LandingPage.vue')
const ProductPage = () => import('../views/ProductPage.vue')
const CheckoutPage = () => import('../views/CheckoutPage.vue')
const AuthPage = () => import('../views/AuthPage.vue')

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage,
  },
  {
    path: '/product',
    name: 'Product',
    component: ProductPage,
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: CheckoutPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: AuthPage,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior() {
    // Always scroll to top when navigating
    return { top: 0 }
  },
})

export default router
