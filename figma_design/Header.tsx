import { Link } from 'react-router-dom';
import { ShoppingCart } from 'lucide-react';
import { useCart } from './CartContext';
import logoImage from 'figma:asset/be9a8d39dab6e5e0332b4a58b19d1ed761635740.png';

export function Header() {
  const { totalItems } = useCart();

  return (
    <header className="bg-[#0f0f0f] border-b border-gray-800 sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-20">
          <Link to="/" className="flex items-center">
            <img src={logoImage} alt="AXYS Logo" className="h-12" />
          </Link>

          <nav className="hidden md:flex items-center gap-8">
            <Link
              to="/"
              className="text-gray-300 hover:text-white transition-colors"
            >
              Home
            </Link>
            <Link
              to="/product"
              className="text-gray-300 hover:text-white transition-colors"
            >
              Product
            </Link>
          </nav>

          <Link
            to="/checkout"
            className="relative p-2 text-gray-300 hover:text-white transition-colors"
          >
            <ShoppingCart className="w-6 h-6" />
            {totalItems > 0 && (
              <span className="absolute -top-1 -right-1 bg-white text-black text-xs rounded-full w-5 h-5 flex items-center justify-center">
                {totalItems}
              </span>
            )}
          </Link>
        </div>
      </div>
    </header>
  );
}
