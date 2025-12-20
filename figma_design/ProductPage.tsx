import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Check, Star, ShoppingCart, Package, Shield, Truck } from 'lucide-react';
import { useCart } from './CartContext';
import productImage from 'figma:asset/94f614937807bde484a291711c5068a375966235.png';

export function ProductPage() {
  const [quantity, setQuantity] = useState(1);
  const { addToCart } = useCart();
  const navigate = useNavigate();

  const product = {
    id: 'axys-cleaner-1',
    name: 'AXYS Premium Golf Cleaner',
    price: 39.99,
    image: productImage,
  };

  const handleAddToCart = () => {
    for (let i = 0; i < quantity; i++) {
      addToCart(product);
    }
    navigate('/checkout');
  };

  return (
    <div className="min-h-screen py-16">
      <div className="container mx-auto px-4">
        <div className="grid md:grid-cols-2 gap-12 mb-16">
          {/* Product Image */}
          <div className="bg-gradient-to-br from-gray-900 to-[#0f0f0f] p-12 flex items-center justify-center border border-gray-800">
            <img
              src={productImage}
              alt={product.name}
              className="w-full h-auto max-w-lg drop-shadow-2xl"
            />
          </div>

          {/* Product Info */}
          <div className="flex flex-col justify-center">
            <div className="flex items-center gap-2 mb-4">
              {[...Array(5)].map((_, i) => (
                <Star key={i} className="w-5 h-5 fill-white text-white" />
              ))}
              <span className="text-gray-400 ml-2">(247 reviews)</span>
            </div>

            <h1 className="text-4xl md:text-5xl mb-4 text-white">
              {product.name}
            </h1>

            <div className="text-3xl mb-6 text-white">
              ${product.price.toFixed(2)}
            </div>

            <p className="text-xl text-gray-400 mb-8">
              The ultimate golf club cleaning solution in a premium, durable container. 
              Designed to attach directly to your golf cart for convenient access throughout your round.
            </p>

            {/* Features List */}
            <div className="space-y-3 mb-8">
              <div className="flex items-center gap-3 text-gray-300">
                <Check className="w-5 h-5 text-white" />
                <span>Premium cleaning formula</span>
              </div>
              <div className="flex items-center gap-3 text-gray-300">
                <Check className="w-5 h-5 text-white" />
                <span>Durable metallic construction</span>
              </div>
              <div className="flex items-center gap-3 text-gray-300">
                <Check className="w-5 h-5 text-white" />
                <span>Universal cart mount included</span>
              </div>
              <div className="flex items-center gap-3 text-gray-300">
                <Check className="w-5 h-5 text-white" />
                <span>Weather-resistant design</span>
              </div>
            </div>

            {/* Quantity Selector */}
            <div className="mb-6">
              <label className="block text-gray-400 mb-2">Quantity</label>
              <div className="flex items-center gap-4">
                <button
                  onClick={() => setQuantity(Math.max(1, quantity - 1))}
                  className="w-10 h-10 border border-gray-700 text-white hover:bg-gray-800 transition-colors"
                >
                  -
                </button>
                <span className="text-xl text-white min-w-[2rem] text-center">{quantity}</span>
                <button
                  onClick={() => setQuantity(quantity + 1)}
                  className="w-10 h-10 border border-gray-700 text-white hover:bg-gray-800 transition-colors"
                >
                  +
                </button>
              </div>
            </div>

            {/* Add to Cart Button */}
            <button
              onClick={handleAddToCart}
              className="w-full bg-white text-black py-4 px-8 hover:bg-gray-200 transition-colors flex items-center justify-center gap-2 mb-4"
            >
              <ShoppingCart className="w-5 h-5" />
              Add to Cart - ${(product.price * quantity).toFixed(2)}
            </button>

            {/* Trust Badges */}
            <div className="grid grid-cols-3 gap-4 pt-8 border-t border-gray-800">
              <div className="text-center">
                <Truck className="w-6 h-6 mx-auto mb-2 text-gray-400" />
                <p className="text-sm text-gray-500">Free Shipping</p>
              </div>
              <div className="text-center">
                <Shield className="w-6 h-6 mx-auto mb-2 text-gray-400" />
                <p className="text-sm text-gray-500">1 Year Warranty</p>
              </div>
              <div className="text-center">
                <Package className="w-6 h-6 mx-auto mb-2 text-gray-400" />
                <p className="text-sm text-gray-500">Ships in 24h</p>
              </div>
            </div>
          </div>
        </div>

        {/* Specifications */}
        <div className="bg-[#0f0f0f] p-8 border border-gray-800">
          <h2 className="text-3xl mb-6 text-white">Specifications</h2>
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-gray-400 mb-2">Dimensions</h3>
              <p className="text-white">4.5" H × 3.2" W</p>
            </div>
            <div>
              <h3 className="text-gray-400 mb-2">Material</h3>
              <p className="text-white">Powder-coated aluminum</p>
            </div>
            <div>
              <h3 className="text-gray-400 mb-2">Capacity</h3>
              <p className="text-white">12 oz cleaning solution</p>
            </div>
            <div>
              <h3 className="text-gray-400 mb-2">Mounting</h3>
              <p className="text-white">Universal cart bracket</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
