<script setup>
import { RouterLink } from 'vue-router'
import { ArrowRight, Droplet, Shield, Sparkles } from 'lucide-vue-next'
</script>

<template>
  <div class="min-h-screen bg-dark-900">
    <!-- Hero Section -->
    <section class="relative overflow-hidden py-24 md:py-32">
      <div class="absolute inset-0 bg-gradient-to-br from-dark-800 via-dark-900 to-black opacity-90"></div>
      <div class="container mx-auto relative z-10">
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <!-- Left: Text -->
          <div>
            <h1 class="text-5xl md:text-7xl font-bold mb-6 text-white">
              Precision Clean.
              <br />
              Flawless Play.
            </h1>
            <p class="text-xl text-gray-400 mb-8 max-w-lg">
              The ultimate golf accessory designed for champions. Keep your equipment pristine with AXYS premium cleaning solution.
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
              <RouterLink
                to="/product"
                class="btn-primary inline-flex items-center justify-center gap-2 group"
              >
                Shop Now
                <ArrowRight class="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </RouterLink>
              <a
                href="#features"
                class="btn-secondary inline-flex items-center justify-center gap-2"
              >
                Learn More
              </a>
            </div>
          </div>
          <!-- Right: Image placeholder -->
          <div class="relative">
            <div class="absolute inset-0 bg-gradient-to-r from-white/10 to-white/5 blur-3xl"></div>
            <div class="relative z-10 w-full h-80 bg-dark-800 border border-dark-700 flex items-center justify-center">
              <span class="text-gray-400">Product Image (Phase 4)</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-24 bg-dark-900">
      <div class="container mx-auto">
        <h2 class="text-4xl md:text-5xl text-center mb-16 text-white">
          Why Choose AXYS?
        </h2>
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="card card-hover">
            <div class="w-12 h-12 bg-white/10 flex items-center justify-center mb-6">
              <Droplet class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-2xl mb-4 text-white">Premium Formula</h3>
            <p class="text-gray-400">
              Our specially formulated solution provides superior cleaning power without damaging your equipment's finish.
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="card card-hover">
            <div class="w-12 h-12 bg-white/10 flex items-center justify-center mb-6">
              <Shield class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-2xl mb-4 text-white">Durable Design</h3>
            <p class="text-gray-400">
              Built with premium materials and a sleek metallic finish that stands up to the demands of the course.
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="card card-hover">
            <div class="w-12 h-12 bg-white/10 flex items-center justify-center mb-6">
              <Sparkles class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-2xl mb-4 text-white">Perfect Results</h3>
            <p class="text-gray-400">
              Experience spotless clubs and improved performance. Your gear deserves the AXYS treatment.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-24">
      <div class="container mx-auto">
        <div class="bg-gradient-to-r from-dark-800 to-dark-900 p-12 md:p-16 text-center border border-dark-700">
          <h2 class="text-4xl md:text-5xl mb-6 text-white">
            Elevate Your Game
          </h2>
          <p class="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">
            Join thousands of golfers who trust AXYS to keep their equipment in pristine condition.
          </p>
          <RouterLink
            to="/product"
            class="btn-primary inline-flex items-center justify-center gap-2"
          >
            Order Now
            <ArrowRight class="w-5 h-5" />
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>
