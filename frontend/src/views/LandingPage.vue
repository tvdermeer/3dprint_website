<script setup>
import { RouterLink } from 'vue-router'
import { ArrowRight, Droplet, Shield, Sparkles } from 'lucide-vue-next'
</script>

<template>
  <div class="min-h-dvh bg-bg-main text-text-main transition-colors duration-300">
    <section class="relative overflow-hidden py-24 md:py-32">
      <!-- Background overlay removed/simplified for theme compatibility -->
      
      <div class="container mx-auto relative z-10 px-6">
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="text-left">
            <h1 class="text-5xl md:text-7xl font-bold mb-6 leading-tight text-balance">
              Precision Clean.
              <br />
              <span class="text-text-main">Flawless Play.</span>
            </h1>
            <p class="text-xl text-text-muted mb-10 max-w-lg leading-relaxed text-pretty">
              The ultimate golf accessory designed for champions. Keep your equipment pristine with AXYS premium cleaning solution.
            </p>
            
            <div class="flex flex-col sm:flex-row gap-5">
              <RouterLink
                to="/product"
                class="btn btn-primary group"
              >
                Shop Now
                <ArrowRight class="size-5 group-hover:translate-x-1 transition-transform" />
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
            <div class="relative z-10 w-full h-80 md:h-[450px] bg-bg-card border border-border-main flex items-center justify-center shadow-2xl transition-colors duration-300">
              <span class="text-text-muted font-medium uppercase">Product Image (Phase 4)</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="features" class="py-24 bg-bg-card transition-colors duration-300">
      <div class="container mx-auto px-6">
        <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-balance">
          Why Choose AXYS?
        </h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="card group">
            <div class="size-14 bg-text-main/5 border border-text-main/10 flex items-center justify-center mb-8 transition-colors group-hover:bg-text-main/10">
              <Droplet class="size-7 text-text-main" />
            </div>
            <h3 class="text-2xl font-bold mb-4 text-balance">Premium Formula</h3>
            <p class="text-text-muted leading-relaxed text-pretty">
              Our specially formulated solution provides superior cleaning power without damaging your equipment's finish.
            </p>
          </div>

          <div class="card group">
            <div class="size-14 bg-text-main/5 border border-text-main/10 flex items-center justify-center mb-8 transition-colors group-hover:bg-text-main/10">
              <Shield class="size-7 text-text-main" />
            </div>
            <h3 class="text-2xl font-bold mb-4 text-balance">Durable Design</h3>
            <p class="text-text-muted leading-relaxed text-pretty">
              Built with premium materials and a sleek metallic finish that stands up to the demands of the course.
            </p>
          </div>

          <div class="card group">
            <div class="size-14 bg-text-main/5 border border-text-main/10 flex items-center justify-center mb-8 transition-colors group-hover:bg-text-main/10">
              <Sparkles class="size-7 text-text-main" />
            </div>
            <h3 class="text-2xl font-bold mb-4 text-balance">Perfect Results</h3>
            <p class="text-text-muted leading-relaxed text-pretty">
              Experience spotless clubs and improved performance. Your gear deserves the AXYS treatment.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24">
      <div class="container mx-auto px-6">
        <div class="bg-bg-card p-12 md:p-24 text-center border border-border-main relative overflow-hidden transition-colors duration-300">
          <div class="relative z-10">
            <h2 class="text-4xl md:text-6xl font-bold mb-8 text-balance">
              Elevate Your Game
            </h2>
            <p class="text-xl text-text-muted mb-12 max-w-2xl mx-auto leading-relaxed text-pretty">
              Join thousands of golfers who trust AXYS to keep their equipment in pristine condition.
            </p>
            <RouterLink
              to="/product"
              class="btn btn-primary"
            >
              Order Now
              <ArrowRight class="ml-2 size-5" />
            </RouterLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
