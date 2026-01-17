<script setup>
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="bg-dark-900 border-t border-dark-700 mt-16 md:mt-24">
    <div class="container py-8 md:py-12">
      <div class="grid md:grid-cols-3 gap-8 mb-8 pb-8 border-b border-dark-700">
        <!-- Brand Section -->
        <div>
          <h3 class="text-white font-bold text-lg mb-4 text-balance">AXYS</h3>
          <p class="text-gray-400 text-sm text-pretty">
            Premium golf club cleaning solution. Precision clean, flawless play.
          </p>
        </div>

        <!-- Links Section -->
        <div>
          <h4 class="text-white font-semibold mb-4 text-balance">Quick Links</h4>
          <ul class="space-y-2">
            <li>
              <RouterLink to="/" class="text-gray-400 hover:text-white transition-colors text-sm">
                Home
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/product" class="text-gray-400 hover:text-white transition-colors text-sm">
                Product
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/checkout" class="text-gray-400 hover:text-white transition-colors text-sm">
                Checkout
              </RouterLink>
            </li>
          </ul>
        </div>

        <!-- Contact Section -->
        <div>
          <h4 class="text-white font-semibold mb-4 text-balance">Support</h4>
          <ul class="space-y-2">
            <li>
              <a href="mailto:support@axys.com" class="text-gray-400 hover:text-white transition-colors text-sm">
                support@axys.com
              </a>
            </li>
            <li>
              <p class="text-gray-400 text-sm tabular-nums">1-800-AXYS-CLEAN</p>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Section -->
      <div class="flex flex-col md:flex-row items-center justify-between text-sm text-gray-500">
        <p class="tabular-nums">&copy; {{ currentYear }} AXYS. All rights reserved.</p>
        <div class="flex gap-6 mt-4 md:mt-0">
          <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
          <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
/* Footer styles */
</style>
