import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Header } from './components/Header';
import { LandingPage } from './components/LandingPage';
import { ProductPage } from './components/ProductPage';
import { CheckoutPage } from './components/CheckoutPage';
import { CartProvider } from './components/CartContext';

export default function App() {
  return (
    <BrowserRouter>
      <CartProvider>
        <div className="min-h-screen bg-[#1a1a1a]">
          <Header />
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/product" element={<ProductPage />} />
            <Route path="/checkout" element={<CheckoutPage />} />
          </Routes>
        </div>
      </CartProvider>
    </BrowserRouter>
  );
}
