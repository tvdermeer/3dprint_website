import { Link } from 'react-router-dom';
import { ArrowRight, Droplet, Shield, Sparkles } from 'lucide-react';
import productImage from 'figma:asset/94f614937807bde484a291711c5068a375966235.png';

export function LandingPage() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-gray-900 via-[#1a1a1a] to-black opacity-90" />
        <div className="container mx-auto px-4 py-24 md:py-32 relative z-10">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h1 className="text-5xl md:text-7xl mb-6 text-white">
                Precision Clean.
                <br />
                Flawless Play.
              </h1>
              <p className="text-xl text-gray-400 mb-8 max-w-lg">
                The ultimate golf accessory designed for champions. Keep your equipment pristine with AXYS premium cleaning solution.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link
                  to="/product"
                  className="inline-flex items-center justify-center gap-2 bg-white text-black px-8 py-4 hover:bg-gray-200 transition-colors group"
                >
                  Shop Now
                  <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </Link>
                <a
                  href="#features"
                  className="inline-flex items-center justify-center gap-2 border border-white text-white px-8 py-4 hover:bg-white hover:text-black transition-colors"
                >
                  Learn More
                </a>
              </div>
            </div>
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-white/10 to-white/5 blur-3xl" />
              <img
                src={productImage}
                alt="AXYS Product"
                className="relative z-10 w-full h-auto drop-shadow-2xl"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-24 bg-[#0f0f0f]">
        <div className="container mx-auto px-4">
          <h2 className="text-4xl md:text-5xl text-center mb-16 text-white">
            Why Choose AXYS?
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="p-8 bg-[#1a1a1a] border border-gray-800 hover:border-gray-700 transition-colors">
              <div className="w-12 h-12 bg-white/10 flex items-center justify-center mb-6">
                <Droplet className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-2xl mb-4 text-white">Premium Formula</h3>
              <p className="text-gray-400">
                Our specially formulated solution provides superior cleaning power without damaging your equipment's finish.
              </p>
            </div>

            <div className="p-8 bg-[#1a1a1a] border border-gray-800 hover:border-gray-700 transition-colors">
              <div className="w-12 h-12 bg-white/10 flex items-center justify-center mb-6">
                <Shield className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-2xl mb-4 text-white">Durable Design</h3>
              <p className="text-gray-400">
                Built with premium materials and a sleek metallic finish that stands up to the demands of the course.
              </p>
            </div>

            <div className="p-8 bg-[#1a1a1a] border border-gray-800 hover:border-gray-700 transition-colors">
              <div className="w-12 h-12 bg-white/10 flex items-center justify-center mb-6">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-2xl mb-4 text-white">Perfect Results</h3>
              <p className="text-gray-400">
                Experience spotless clubs and improved performance. Your gear deserves the AXYS treatment.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24">
        <div className="container mx-auto px-4">
          <div className="bg-gradient-to-r from-gray-800 to-gray-900 p-12 md:p-16 text-center border border-gray-700">
            <h2 className="text-4xl md:text-5xl mb-6 text-white">
              Elevate Your Game
            </h2>
            <p className="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">
              Join thousands of golfers who trust AXYS to keep their equipment in pristine condition.
            </p>
            <Link
              to="/product"
              className="inline-flex items-center justify-center gap-2 bg-white text-black px-8 py-4 hover:bg-gray-200 transition-colors"
            >
              Order Now
              <ArrowRight className="w-5 h-5" />
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
