<script setup>
import { RouterLink } from 'vue-router'
import { ArrowRight, Droplet, Shield, Sparkles } from 'lucide-vue-next'
</script>

<template>
  <div class="min-h-screen bg-dark-900 text-white">
    <section class="relative overflow-hidden py-24 md:py-32">
      <div class="absolute inset-0 bg-gradient-to-br from-dark-800 via-dark-900 to-black opacity-90"></div>
      
      <div class="container mx-auto relative z-10 px-6">
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="text-left">
            <h1 class="text-5xl md:text-7xl font-bold mb-6 leading-tight tracking-tight">
              Precision Clean.
              <br />
              <span class="text-white">Flawless Play.</span>
            </h1>
            <p class="text-xl text-secondary mb-10 max-w-lg leading-relaxed">
              The ultimate golf accessory designed for champions. Keep your equipment pristine with AXYS premium cleaning solution.
            </p>
            
            <div class="flex flex-col sm:flex-row gap-5">
              <RouterLink
                to="/product"
                class="btn btn-primary group"
              >
                Shop Now
                <ArrowRight class="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </RouterLink>
              <a
                href="#features"
                class="btn btn-secondary"
              >
                Learn More
              </a>
            </div>
          </div>

          <div class="relative">
            <div class="absolute inset-0 bg-white/5 blur-3xl rounded-full"></div>
            <div class="relative z-10 w-full h-80 md:h-[450px] bg-dark-800 border border-dark-700 flex items-center justify-center shadow-2xl">
              <span class="text-secondary font-medium tracking-widest uppercase">Product Image (Phase 4)</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="features" class="py-24 bg-black/20">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 tracking-tight">
          Why Choose AXYS?
        </h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="card card-hover group">
            <div class="w-14 h-14 bg-white/5 border border-white/10 flex items-center justify-center mb-8 transition-colors group-hover:bg-white/10">
              <Droplet class="w-7 h-7 text-white" />
            </div>
            <h3 class="text-2xl font-bold mb-4">Premium Formula</h3>
            <p class="text-secondary leading-relaxed">
              Our specially formulated solution provides superior cleaning power without damaging your equipment's finish.
            </p>
          </div>

          <div class="card card-hover group">
            <div class="w-14 h-14 bg-white/5 border border-white/10 flex items-center justify-center mb-8 transition-colors group-hover:bg-white/10">
              <Shield class="w-7 h-7 text-white" />
            </div>
            <h3 class="text-2xl font-bold mb-4">Durable Design</h3>
            <p class="text-secondary leading-relaxed">
              Built with premium materials and a sleek metallic finish that stands up to the demands of the course.
            </p>
          </div>

          <div class="card card-hover group">
            <div class="w-14 h-14 bg-white/5 border border-white/10 flex items-center justify-center mb-8 transition-colors group-hover:bg-white/10">
              <Sparkles class="w-7 h-7 text-white" />
            </div>
            <h3 class="text-2xl font-bold mb-4">Perfect Results</h3>
            <p class="text-secondary leading-relaxed">
              Experience spotless clubs and improved performance. Your gear deserves the AXYS treatment.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24">
      <div class="container mx-auto px-6">
        <div class="bg-gradient-to-b from-dark-800 to-dark-900 p-12 md:p-24 text-center border border-dark-700 relative overflow-hidden">
          <div class="relative z-10">
            <h2 class="text-4xl md:text-6xl font-bold mb-8 tracking-tight">
              Elevate Your Game
            </h2>
            <p class="text-xl text-secondary mb-12 max-w-2xl mx-auto leading-relaxed">
              Join thousands of golfers who trust AXYS to keep their equipment in pristine condition.
            </p>
            <RouterLink
              to="/product"
              class="btn btn-primary"
            >
              Order Now
              <ArrowRight class="ml-2 w-5 h-5" />
            </RouterLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>