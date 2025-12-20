import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Trash2, ArrowLeft, CreditCard, Lock } from 'lucide-react';
import { useCart } from './CartContext';

export function CheckoutPage() {
  const { items, removeFromCart, updateQuantity, totalPrice, clearCart } = useCart();
  const [step, setStep] = useState<'cart' | 'payment' | 'success'>('cart');
  const [formData, setFormData] = useState({
    email: '',
    name: '',
    address: '',
    city: '',
    zipCode: '',
    cardNumber: '',
    expiryDate: '',
    cvv: '',
  });

  const shippingCost = totalPrice > 0 ? 9.99 : 0;
  const tax = totalPrice * 0.08;
  const finalTotal = totalPrice + shippingCost + tax;

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handlePlaceOrder = (e: React.FormEvent) => {
    e.preventDefault();
    setStep('success');
    setTimeout(() => {
      clearCart();
    }, 3000);
  };

  if (step === 'success') {
    return (
      <div className="min-h-screen py-16">
        <div className="container mx-auto px-4 max-w-2xl">
          <div className="bg-[#0f0f0f] p-12 border border-gray-800 text-center">
            <div className="w-16 h-16 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg
                className="w-8 h-8 text-green-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M5 13l4 4L19 7"
                />
              </svg>
            </div>
            <h1 className="text-4xl mb-4 text-white">Order Confirmed!</h1>
            <p className="text-xl text-gray-400 mb-8">
              Thank you for your purchase. Your order has been successfully placed.
            </p>
            <p className="text-gray-500 mb-8">
              You will receive a confirmation email shortly with tracking information.
            </p>
            <Link
              to="/"
              className="inline-flex items-center gap-2 bg-white text-black px-8 py-3 hover:bg-gray-200 transition-colors"
            >
              <ArrowLeft className="w-5 h-5" />
              Back to Home
            </Link>
          </div>
        </div>
      </div>
    );
  }

  if (items.length === 0) {
    return (
      <div className="min-h-screen py-16">
        <div className="container mx-auto px-4 max-w-2xl">
          <div className="bg-[#0f0f0f] p-12 border border-gray-800 text-center">
            <h1 className="text-4xl mb-4 text-white">Your Cart is Empty</h1>
            <p className="text-xl text-gray-400 mb-8">
              Add some items to your cart to get started.
            </p>
            <Link
              to="/product"
              className="inline-flex items-center gap-2 bg-white text-black px-8 py-3 hover:bg-gray-200 transition-colors"
            >
              Shop Now
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen py-16">
      <div className="container mx-auto px-4">
        <div className="max-w-6xl mx-auto">
          <div className="mb-8">
            <Link
              to="/product"
              className="inline-flex items-center gap-2 text-gray-400 hover:text-white transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Continue Shopping
            </Link>
          </div>

          <h1 className="text-4xl md:text-5xl mb-8 text-white">
            {step === 'cart' ? 'Shopping Cart' : 'Checkout'}
          </h1>

          <div className="grid md:grid-cols-3 gap-8">
            {/* Cart Items / Payment Form */}
            <div className="md:col-span-2">
              {step === 'cart' ? (
                <div className="space-y-4">
                  {items.map((item) => (
                    <div
                      key={item.id}
                      className="bg-[#0f0f0f] p-6 border border-gray-800 flex gap-6"
                    >
                      <img
                        src={item.image}
                        alt={item.name}
                        className="w-24 h-24 object-contain bg-gray-900"
                      />
                      <div className="flex-1">
                        <h3 className="text-xl mb-2 text-white">{item.name}</h3>
                        <p className="text-gray-400 mb-4">${item.price.toFixed(2)}</p>
                        <div className="flex items-center gap-4">
                          <button
                            onClick={() => updateQuantity(item.id, item.quantity - 1)}
                            className="w-8 h-8 border border-gray-700 text-white hover:bg-gray-800 transition-colors"
                          >
                            -
                          </button>
                          <span className="text-white">{item.quantity}</span>
                          <button
                            onClick={() => updateQuantity(item.id, item.quantity + 1)}
                            className="w-8 h-8 border border-gray-700 text-white hover:bg-gray-800 transition-colors"
                          >
                            +
                          </button>
                        </div>
                      </div>
                      <div className="flex flex-col items-end justify-between">
                        <button
                          onClick={() => removeFromCart(item.id)}
                          className="text-gray-400 hover:text-red-500 transition-colors"
                        >
                          <Trash2 className="w-5 h-5" />
                        </button>
                        <p className="text-xl text-white">
                          ${(item.price * item.quantity).toFixed(2)}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <form onSubmit={handlePlaceOrder} className="bg-[#0f0f0f] p-8 border border-gray-800">
                  <h2 className="text-2xl mb-6 text-white flex items-center gap-2">
                    <CreditCard className="w-6 h-6" />
                    Payment Information
                  </h2>
                  
                  <div className="space-y-4">
                    <div>
                      <label className="block text-gray-400 mb-2">Email</label>
                      <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleInputChange}
                        required
                        className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                        placeholder="your@email.com"
                      />
                    </div>

                    <div>
                      <label className="block text-gray-400 mb-2">Full Name</label>
                      <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleInputChange}
                        required
                        className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                        placeholder="John Doe"
                      />
                    </div>

                    <div>
                      <label className="block text-gray-400 mb-2">Address</label>
                      <input
                        type="text"
                        name="address"
                        value={formData.address}
                        onChange={handleInputChange}
                        required
                        className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                        placeholder="123 Main St"
                      />
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <label className="block text-gray-400 mb-2">City</label>
                        <input
                          type="text"
                          name="city"
                          value={formData.city}
                          onChange={handleInputChange}
                          required
                          className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                          placeholder="New York"
                        />
                      </div>
                      <div>
                        <label className="block text-gray-400 mb-2">ZIP Code</label>
                        <input
                          type="text"
                          name="zipCode"
                          value={formData.zipCode}
                          onChange={handleInputChange}
                          required
                          className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                          placeholder="10001"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="block text-gray-400 mb-2">Card Number</label>
                      <input
                        type="text"
                        name="cardNumber"
                        value={formData.cardNumber}
                        onChange={handleInputChange}
                        required
                        maxLength={16}
                        className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                        placeholder="1234 5678 9012 3456"
                      />
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <label className="block text-gray-400 mb-2">Expiry Date</label>
                        <input
                          type="text"
                          name="expiryDate"
                          value={formData.expiryDate}
                          onChange={handleInputChange}
                          required
                          placeholder="MM/YY"
                          className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                        />
                      </div>
                      <div>
                        <label className="block text-gray-400 mb-2">CVV</label>
                        <input
                          type="text"
                          name="cvv"
                          value={formData.cvv}
                          onChange={handleInputChange}
                          required
                          maxLength={3}
                          className="w-full bg-[#1a1a1a] border border-gray-700 text-white px-4 py-3 focus:outline-none focus:border-white"
                          placeholder="123"
                        />
                      </div>
                    </div>
                  </div>

                  <div className="mt-6 p-4 bg-[#1a1a1a] border border-gray-700 flex items-center gap-2 text-sm text-gray-400">
                    <Lock className="w-4 h-4" />
                    Your payment information is secure and encrypted
                  </div>
                </form>
              )}
            </div>

            {/* Order Summary */}
            <div>
              <div className="bg-[#0f0f0f] p-6 border border-gray-800 sticky top-24">
                <h2 className="text-2xl mb-6 text-white">Order Summary</h2>
                
                <div className="space-y-3 mb-6 pb-6 border-b border-gray-800">
                  <div className="flex justify-between text-gray-400">
                    <span>Subtotal</span>
                    <span>${totalPrice.toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between text-gray-400">
                    <span>Shipping</span>
                    <span>${shippingCost.toFixed(2)}</span>
                  </div>
                  <div className="flex justify-between text-gray-400">
                    <span>Tax</span>
                    <span>${tax.toFixed(2)}</span>
                  </div>
                </div>

                <div className="flex justify-between text-2xl mb-6 text-white">
                  <span>Total</span>
                  <span>${finalTotal.toFixed(2)}</span>
                </div>

                {step === 'cart' ? (
                  <button
                    onClick={() => setStep('payment')}
                    className="w-full bg-white text-black py-3 px-6 hover:bg-gray-200 transition-colors"
                  >
                    Proceed to Checkout
                  </button>
                ) : (
                  <button
                    type="submit"
                    onClick={handlePlaceOrder}
                    className="w-full bg-white text-black py-3 px-6 hover:bg-gray-200 transition-colors"
                  >
                    Place Order
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
