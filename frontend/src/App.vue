<script setup>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div id="app" class="flex flex-col min-h-dvh bg-dark-900 text-primary">
    <!-- Header (sticky) -->
    <Header />

    <!-- Main content (grows to fill space) -->
    <main class="flex-1">
      <RouterView />
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>


