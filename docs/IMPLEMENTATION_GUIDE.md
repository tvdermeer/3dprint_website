# AXYS Golf Cleaner - Frontend Implementation Guide

## Overview

This document outlines the step-by-step implementation of the AXYS Golf Cleaner e-commerce website based on the Figma design. The frontend is built with **Vue 3**, **Vite**, **Pinia** (state management), and **Tailwind CSS** for styling.

---

## Design Summary

### Visual Design
- **Color Scheme**: Dark theme (primary: #0f0f0f, secondary: #1a1a1a, accents: white/gray)
- **Product**: AXYS Premium Golf Cleaner ($39.99)
- **Tagline**: "Precision Clean. Flawless Play."
- **Brand**: Premium golf equipment accessory

### Pages to Implement
1. **Landing Page** (`/`) - Hero, features, CTA sections
2. **Product Page** (`/product`) - Product details, add to cart
3. **Checkout Page** (`/checkout`) - Cart, payment form, order confirmation

### Key Features
- Shopping cart with persistent state
- Multi-step checkout flow
- Product quantity selector
- Order summary with tax & shipping calculation
- Responsive design (mobile-first)

---

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.vue              # Navigation, logo, cart badge
│   │   ├── Footer.vue              # Footer (optional)
│   │   ├── ProductCard.vue         # Reusable product card
│   │   └── QuantitySelector.vue    # +/- quantity control
│   ├── views/
│   │   ├── LandingPage.vue         # Home page
│   │   ├── ProductPage.vue         # Product details
│   │   └── CheckoutPage.vue        # Cart & checkout
│   ├── stores/
│   │   ├── cart.js                 # Pinia cart store
│   │   └── product.js              # Pinia product store (optional)
│   ├── assets/
│   │   ├── images/
│   │   │   ├── product.png         # Product image
│   │   │   └── logo.png            # AXYS logo
│   │   └── css/
│   │       └── globals.css         # Global styles
│   ├── router/
│   │   └── index.js                # Vue Router configuration
│   ├── App.vue                     # Root component
│   └── main.js                     # Entry point
├── public/
├── index.html
├── vite.config.js                  # Vite configuration
├── tailwind.config.js              # Tailwind configuration
├── postcss.config.js               # PostCSS configuration
├── package.json                    # Dependencies
└── .env.example                    # Environment variables template
```

---

## Phase Breakdown

### Phase 1: Project Setup & Structure

#### 1.1 Update Dependencies

**Install required packages:**
```bash
npm install vue-router pinia lucide-vue-next
npm install -D tailwindcss postcss autoprefixer
```

**Update `package.json` scripts:**
```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext .vue,.js,.jsx,.cjs,.mjs --fix --ignore-path .gitignore"
  }
}
```

#### 1.2 Tailwind CSS Setup

**Initialize Tailwind:**
```bash
npx tailwindcss init -p
```

**Configure `tailwind.config.js`:**
- Set dark theme as default
- Define custom colors matching the design
- Configure spacing and typography

#### 1.3 File Structure

Create the following directories:
```bash
mkdir -p src/{components,views,stores,assets/{images,css},router}
```

---

### Phase 2: Core Components & Layouts

#### 2.1 Header Component (`src/components/Header.vue`)

**Features:**
- Sticky header with navigation
- Logo (AXYS) on the left
- Navigation links (Home, Product)
- Shopping cart icon with badge showing item count

**Implementation Details:**
- Use `lucide-vue-next` for ShoppingCart icon
- Display cart badge only when items exist
- Link to `/checkout` when clicking cart

#### 2.2 Footer Component (`src/components/Footer.vue`)

**Features:**
- Simple footer (optional, can be minimal)
- Links, copyright info

---

### Phase 3: Pinia Store (State Management)

#### 3.1 Cart Store (`src/stores/cart.js`)

**State:**
```javascript
{
  items: [
    {
      id: string,
      name: string,
      price: number,
      quantity: number,
      image: string
    }
  ]
}
```

**Actions:**
- `addToCart(item)` - Add item or increment quantity
- `removeFromCart(id)` - Remove item from cart
- `updateQuantity(id, quantity)` - Update item quantity
- `clearCart()` - Empty the entire cart

**Getters:**
- `totalItems` - Sum of all quantities
- `totalPrice` - Sum of (price × quantity) for all items
- `cartItems` - The items array

**Features:**
- Persist cart to localStorage
- Restore cart from localStorage on app load

---

### Phase 4: Landing Page (`src/views/LandingPage.vue`)

**Sections:**

#### 4.1 Hero Section
- Large headline: "Precision Clean. Flawless Play."
- Subheading: "The ultimate golf accessory..."
- Two CTAs: "Shop Now" (primary), "Learn More" (secondary)
- Product image on the right
- Dark gradient background

#### 4.2 Features Section
Three feature cards:
1. **Premium Formula** (Droplet icon)
2. **Durable Design** (Shield icon)
3. **Perfect Results** (Sparkles icon)

Each card includes:
- Icon
- Title
- Description

#### 4.3 CTA Section
- "Elevate Your Game" headline
- Description: "Join thousands of golfers..."
- "Order Now" button

**Styling:**
- Responsive grid (1 col mobile, 2 cols tablet, 2 cols desktop)
- Dark theme with subtle borders
- Hover effects on cards and buttons

---

### Phase 5: Product Page (`src/views/ProductPage.vue`)

**Layout:** Two-column grid (image left, info right)

#### 5.1 Product Image Section
- Dark gradient background
- Product image centered
- Responsive sizing

#### 5.2 Product Information
- 5-star rating with review count: ⭐⭐⭐⭐⭐ (247 reviews)
- Product name: "AXYS Premium Golf Cleaner"
- Price: $39.99 (large text)
- Description paragraph

#### 5.3 Features List
Bulleted list with checkmark icons:
- Premium cleaning formula
- Durable metallic construction
- Universal cart mount included
- Weather-resistant design

#### 5.4 Quantity Selector
- Label: "Quantity"
- `-` button, quantity display, `+` button
- Minimum quantity: 1

#### 5.5 Add to Cart Button
- Full-width button
- Text: "Add to Cart - $39.99" (dynamic price)
- On click: add to cart, navigate to checkout

#### 5.6 Trust Badges
Three columns:
- Truck icon + "Free Shipping"
- Shield icon + "1 Year Warranty"
- Package icon + "Ships in 24h"

#### 5.7 Specifications Section
A two-column grid:
- Dimensions: 4.5" H × 3.2" W
- Material: Powder-coated aluminum
- Capacity: 12 oz cleaning solution
- Mounting: Universal cart bracket

---

### Phase 6: Checkout Page (`src/views/CheckoutPage.vue`)

**Multi-step flow:** cart → payment → success

#### 6.1 Step 1: Shopping Cart
- Product list (each item shows image, name, price, quantity controls, remove button)
- Order summary sidebar:
  - Subtotal
  - Shipping ($9.99)
  - Tax (8%)
  - **Total**
  - "Proceed to Checkout" button

#### 6.2 Step 2: Payment Form
- Email input
- Full Name input
- Address input
- City input
- ZIP Code input
- Card Number input (max 16 chars)
- Expiry Date input (MM/YY)
- CVV input (max 3 chars)
- Security badge: "Your payment information is secure and encrypted"
- Order summary sidebar (same as Step 1)
- "Place Order" button

#### 6.3 Step 3: Success Screen
- Green checkmark icon
- "Order Confirmed!" heading
- Confirmation message
- "Back to Home" button
- Auto-clear cart after 3 seconds

#### 6.4 Empty Cart State
- Show when cart is empty
- "Your Cart is Empty" heading
- "Add some items to your cart to get started"
- "Shop Now" button linking to `/product`

---

### Phase 7: Styling & Polish

#### 7.1 Global Styles
- Reset default browser styles
- Define Tailwind custom colors
- Typography scales
- Spacing system

#### 7.2 Dark Theme Colors
```css
Primary background: #0f0f0f
Secondary background: #1a1a1a
Border color: #2a2a2a (gray-800)
Text primary: #ffffff
Text secondary: #a0a0a0 (gray-400)
Accent: #ffffff
Success: #10b981 (green)
```

#### 7.3 Responsive Design
- Mobile: Single column layouts, stacked sections
- Tablet (768px): Two-column layouts start
- Desktop (1024px): Full multi-column layouts

#### 7.4 Hover & Transitions
- Button hover: opacity/background color change
- Card hover: border color change
- Smooth transitions (200-300ms)

---

### Phase 8: Integration & Testing

#### 8.1 Test Scenarios
- **Cart functionality:**
  - Add item to cart
  - Remove item from cart
  - Update quantity
  - Clear cart
  - Cart persists after page refresh

- **Checkout flow:**
  - Navigate from product page to checkout
  - View cart with correct totals
  - Submit payment form
  - See success screen
  - Cart clears after success

- **Responsive design:**
  - Test on mobile (375px), tablet (768px), desktop (1440px)
  - All text readable
  - Images scale properly
  - Buttons clickable (no small touch targets)

- **Navigation:**
  - Home → Product → Checkout
  - Back buttons work correctly
  - Cart badge updates

---

### Phase 9: Documentation & Deployment

#### 9.1 Component Documentation
Document each component with:
- Purpose
- Props (if any)
- Events (if any)
- Example usage

#### 9.2 Store Documentation
Document Pinia stores:
- State structure
- Available actions
- Available getters

#### 9.3 Environment Variables
Create `.env.example`:
```
VITE_API_BASE_URL=http://localhost:8000
VITE_STRIPE_PUBLIC_KEY=pk_test_...
```

---

## Implementation Checklist

### Phase 1: Setup
- [ ] Install dependencies
- [ ] Configure Tailwind CSS
- [ ] Create folder structure
- [ ] Set up Vue Router
- [ ] Set up Vite configuration

### Phase 2: Components
- [ ] Create Header component
- [ ] Create Footer component
- [ ] Create base layout

### Phase 3: State Management
- [ ] Create Pinia cart store
- [ ] Add localStorage persistence
- [ ] Test store functionality

### Phase 4-6: Pages
- [ ] Landing Page implementation
- [ ] Product Page implementation
- [ ] Checkout Page implementation

### Phase 7: Styling
- [ ] Apply Tailwind CSS throughout
- [ ] Ensure responsive design
- [ ] Add hover/transition effects

### Phase 8: Testing
- [ ] Manual testing of all flows
- [ ] Responsive testing (mobile/tablet/desktop)
- [ ] Cross-browser testing

### Phase 9: Documentation
- [ ] Write component docs
- [ ] Write setup instructions
- [ ] Prepare for API integration

---

## Key Design Tokens

### Colors
- **Background**: `#0f0f0f` (dark-900)
- **Card Background**: `#1a1a1a` (dark-800)
- **Border**: `#2a2a2a` (gray-800)
- **Text Primary**: `#ffffff` (white)
- **Text Secondary**: `#a0a0a0` (gray-400)

### Typography
- **Hero Title**: 48px / 64px (mobile / desktop)
- **Section Title**: 36px / 48px
- **Body**: 16px
- **Small**: 14px

### Spacing
- **Container Max Width**: 1024px
- **Padding (horizontal)**: 16px (mobile), 24px (desktop)
- **Gap**: 32px (sections), 16px (items)

### Border Radius
- Minimal (0-4px mostly), modern flat design

---

## Next Steps

1. **Start Phase 1** - Set up dependencies and folder structure
2. **Build Phase 2** - Create reusable components
3. **Implement Phase 3** - Set up Pinia cart store
4. **Develop Phases 4-6** - Create the three pages
5. **Polish Phase 7** - Ensure dark theme consistency and responsiveness
6. **Test Phase 8** - Thoroughly test all user flows
7. **Document Phase 9** - Prepare for API integration

Each phase should be completed before moving to the next to ensure a solid foundation.

---

## Notes for Future Enhancement

- **Backend Integration**: Currently using hardcoded product data. Replace with API calls to FastAPI backend.
- **Payment Processing**: Currently mock payment form. Integrate with Stripe API.
- **Image Optimization**: Implement lazy loading and image compression.
- **SEO**: Add meta tags, Open Graph, structured data.
- **Analytics**: Integrate Google Analytics or similar.
- **Multi-Product Support**: Extend stores and pages for multiple products.

---

**Last Updated:** 2025-12-20
**Author:** Implementation Guide for AXYS Golf Cleaner
