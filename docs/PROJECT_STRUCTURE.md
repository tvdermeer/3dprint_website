# AXYS Project Structure & Architecture

## Visual Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    AXYS E-Commerce Site                     │
│                   (Vue 3 + Pinia + Vite)                    │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                │             │             │
          ┌─────▼──────┐  ┌───▼──────┐  ┌──▼─────────┐
          │  Router    │  │ State    │  │ Components │
          │            │  │ (Pinia)  │  │            │
          └─────┬──────┘  └───┬──────┘  └──┬─────────┘
                │             │            │
         ┌──────┼──────┐      │      ┌─────┼────────┐
         │      │      │      │      │     │        │
      ┌──▼─┐ ┌─▼─┐ ┌──▼──┐   │    ┌─▼──┐ │  ┌────▼──┐
      │ / │ │/  │ │/    │   │    │Head││  │  │ Other │
      │   │ │ P │ │Check│   │    │er  │◄─┘  │  UI   │
      │ H │ │ R │ │out  │   │    │    │     │       │
      │ o │ │ O │ │     │   │    └────┘     │       │
      │ m │ │ D │ │     │   │               │       │
      │ e │ │   │ │     │   │           ┌───▼────┐  │
      └──┬─ └─┬─ └─────┬─   │      ┌────▼──┐    │  │
         │   │   │         │      │Product │    │  │
         │   │   │     ┌───▼──────┤ Store  │    │  │
         │   │   │     │   ┌──────┴────────┘    │  │
         │   │   │     │   │              ┌─────▼──┘
         │   │   │  ┌──▼───▼──┐           │
         │   │   │  │  Cart   │           │
         │   │   └─►│  Store  │◄──────────┘
         │   │      │         │
         │   │      └────┬────┘
         │   │           │
         │   └──────┬────┤ (localStorage)
         │          │    │
         └──────┬───┘    │
                │        │
            ┌───▼────────▼──────┐
            │  Browser Storage  │
            │  (localStorage)   │
            └───────────────────┘
```

---

## Directory Tree

```
3dprint_website/
│
├── frontend/                          # Vue 3 Frontend App
│   ├── src/
│   │   ├── assets/
│   │   │   ├── css/
│   │   │   │   └── globals.css       # Global Tailwind styles
│   │   │   └── images/
│   │   │       ├── product.png       # Product image
│   │   │       └── logo.png          # AXYS logo
│   │   │
│   │   ├── components/               # Reusable components
│   │   │   ├── Header.vue            # Navigation + cart badge
│   │   │   ├── Footer.vue            # Footer (optional)
│   │   │   ├── QuantitySelector.vue  # +/- quantity control
│   │   │   └── ProductCard.vue       # Reusable product card
│   │   │
│   │   ├── views/                    # Page-level components
│   │   │   ├── LandingPage.vue       # Home page (/)
│   │   │   ├── ProductPage.vue       # Product page (/product)
│   │   │   └── CheckoutPage.vue      # Checkout page (/checkout)
│   │   │
│   │   ├── stores/                   # Pinia state management
│   │   │   ├── cart.js               # Cart store (main)
│   │   │   └── product.js            # Product store (optional)
│   │   │
│   │   ├── router/
│   │   │   └── index.js              # Vue Router configuration
│   │   │
│   │   ├── App.vue                   # Root component
│   │   └── main.js                   # App entry point
│   │
│   ├── public/                        # Static assets
│   ├── index.html                    # HTML template
│   ├── package.json                  # Dependencies
│   ├── vite.config.js                # Vite configuration
│   ├── tailwind.config.js            # Tailwind CSS config
│   ├── postcss.config.js             # PostCSS config
│   ├── .env.example                  # Environment template
│   └── .env                          # Environment (git-ignored)
│
├── backend/                           # FastAPI Backend
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── core/
│   │   └── main.py
│   │
│   ├── migrations/
│   ├── requirements.txt
│   ├── alembic.ini
│   └── .env.example
│
├── figma_design/                     # Design source files
│   ├── LandingPage.tsx               # React design component
│   ├── ProductPage.tsx               # React design component
│   ├── CheckoutPage.tsx              # React design component
│   ├── Header.tsx                    # React design component
│   ├── CartContext.tsx               # React state management
│   ├── component/ (*.tsx)            # UI component library
│   ├── *.png                         # Design images & mockups
│   └── *.css                         # Design styles
│
├── IMPLEMENTATION_GUIDE.md            # Phase-by-phase guide
├── DESIGN_SPECS.md                    # Complete style guide
├── IMPLEMENTATION_SUMMARY.md          # Project overview
├── QUICK_REFERENCE.md                 # Quick lookup card
├── PROJECT_STRUCTURE.md               # This file
├── WORK_LOG.md                        # Progress tracking
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Component Hierarchy

```
App.vue (Root)
│
├── Header
│   ├── Logo (image)
│   ├── Nav Links
│   │   ├── Home (/)
│   │   └── Product (/product)
│   └── Cart Icon
│       └── Badge (totalItems count)
│
├── RouterView
│   ├── LandingPage (/)
│   │   ├── Hero Section
│   │   │   ├── Headline + Description
│   │   │   ├── CTA Buttons
│   │   │   └── Product Image
│   │   ├── Features Section
│   │   │   ├── Feature Card 1
│   │   │   ├── Feature Card 2
│   │   │   └── Feature Card 3
│   │   └── CTA Section
│   │       ├── Headline
│   │       ├── Description
│   │       └── CTA Button
│   │
│   ├── ProductPage (/product)
│   │   ├── Product Image
│   │   │   └── Gallery Area
│   │   ├── Product Info
│   │   │   ├── Rating + Reviews
│   │   │   ├── Name + Price
│   │   │   ├── Description
│   │   │   ├── Features List
│   │   │   ├── QuantitySelector
│   │   │   ├── Add to Cart Button
│   │   │   ├── Trust Badges
│   │   │   └── Specifications
│   │   └── [Not implemented yet]
│   │
│   └── CheckoutPage (/checkout)
│       ├── Cart Items View
│       │   └── Product List
│       │       ├── Product 1
│       │       │   ├── Image
│       │       │   ├── Name + Price
│       │       │   ├── QuantitySelector
│       │       │   └── Remove Button
│       │       └── [More products...]
│       ├── Order Summary Sidebar
│       │   ├── Subtotal
│       │   ├── Shipping
│       │   ├── Tax
│       │   ├── Total
│       │   └── CTA Button
│       ├── Payment Form
│       │   ├── Email Input
│       │   ├── Name Input
│       │   ├── Address Inputs
│       │   ├── Card Inputs
│       │   └── Security Badge
│       └── Success Screen
│           ├── Success Icon
│           ├── Confirmation Message
│           └── Back to Home Button
│
└── Footer
    └── [Footer content]
```

---

## Data Flow

### User Adding Product to Cart

```
User clicks "Add to Cart"
        │
        ▼
ProductPage component
        │
        ├─► useCartStore()
        │
        └─► cart.addToCart({
                id, name, price, image
            })
            │
            ▼
        Cart Store
            │
            ├─► Update state.items
            ├─► Recalculate getters
            │   (totalItems, totalPrice)
            └─► Auto-save to localStorage
                │
                ▼
            Header component receives
            updated totalItems
            (via store subscription)
            │
            ▼
            Cart badge updates in UI
```

### User Navigating to Checkout

```
User at ProductPage
        │
        ├─► Click "Add to Cart"
        │
        ├─► Navigate to /checkout
        │
        ▼
CheckoutPage loads
        │
        ├─► useCartStore()
        │   (cart already populated
        │    from previous step)
        │
        ├─► Display cart.items
        │
        ├─► Display calculations:
        │   - subtotal
        │   - shipping ($9.99)
        │   - tax (8%)
        │   - total
        │
        └─► User proceeds through
            checkout steps
```

### Form Submission Flow

```
Payment Form Submit
        │
        ▼
Validate form data
        │
        ├─► Check required fields
        ├─► Validate email format
        ├─► Validate card format
        │
        ▼ (if valid)
Set checkout step to "success"
        │
        ├─► Display success screen
        ├─► Show order confirmation
        │
        ├─► Schedule auto-action
        │   (after 3 seconds)
        │
        └─► cart.clearCart()
            │
            ▼
        localStorage updated
            │
            ▼
        Cart badge disappears
            │
            ▼
        Navigate back to home
```

---

## State Management (Pinia Cart Store)

### Store Structure

```javascript
useCartStore()
│
├── State
│   └── items: [
│       {
│         id: string,
│         name: string,
│         price: number,
│         quantity: number,
│         image: string
│       },
│       ...
│     ]
│
├── Getters
│   ├── totalItems: number
│   ├── totalPrice: number
│   └── cartItems: CartItem[]
│
├── Actions
│   ├── addToCart(item)
│   ├── removeFromCart(id)
│   ├── updateQuantity(id, qty)
│   ├── clearCart()
│   ├── loadFromLocalStorage()
│   └── saveToLocalStorage()
│
└── Persistence
    └── localStorage('axys-cart')
```

---

## Page Layouts

### Landing Page Layout
```
┌──────────────────────────────────────────┐
│              HEADER                       │
├──────────────────────────────────────────┤
│                                          │
│  ┌────────────┐     ┌─────────────────┐ │
│  │  Headline  │     │                 │ │
│  │  Copy      │     │  Product Image  │ │
│  │  Buttons   │     │                 │ │
│  └────────────┘     └─────────────────┘ │
│                                          │
│  ┌──────────────────────────────────────┐│
│  │  Why Choose AXYS?                    ││
│  │  ┌────────┐ ┌────────┐ ┌────────┐  ││
│  │  │ Card 1 │ │ Card 2 │ │ Card 3 │  ││
│  │  └────────┘ └────────┘ └────────┘  ││
│  └──────────────────────────────────────┘│
│                                          │
│  ┌──────────────────────────────────────┐│
│  │  Elevate Your Game (CTA Section)     ││
│  │  [Order Now Button]                  ││
│  └──────────────────────────────────────┘│
│                                          │
├──────────────────────────────────────────┤
│              FOOTER                      │
└──────────────────────────────────────────┘
```

### Product Page Layout
```
┌──────────────────────────────────────────┐
│              HEADER                       │
├──────────────────────────────────────────┤
│                                          │
│  ┌─────────────┐  ┌─────────────────┐  │
│  │             │  │  ⭐⭐⭐⭐⭐       │  │
│  │             │  │  AXYS Cleaner   │  │
│  │   Product   │  │  $39.99         │  │
│  │   Image     │  │  Description    │  │
│  │             │  │  ✓ Feature 1    │  │
│  │             │  │  ✓ Feature 2    │  │
│  │             │  │  ✓ Feature 3    │  │
│  │             │  │  Qty: [- 1 +]   │  │
│  │             │  │  [Add to Cart]  │  │
│  │             │  │  Trust Badges   │  │
│  └─────────────┘  └─────────────────┘  │
│                                          │
│  ┌──────────────────────────────────────┐│
│  │ Specifications                       ││
│  │ Dimensions | Material                ││
│  │ Capacity   | Mounting                ││
│  └──────────────────────────────────────┘│
│                                          │
├──────────────────────────────────────────┤
│              FOOTER                      │
└──────────────────────────────────────────┘
```

### Checkout Page Layout
```
┌──────────────────────────────────────────┐
│              HEADER                       │
├──────────────────────────────────────────┤
│                                          │
│  Continue Shopping                       │
│  ┌─────────────────────┐  ┌───────────┐ │
│  │                     │  │  Summary  │ │
│  │  Cart Items         │  │           │ │
│  │  ┌───────────────┐  │  │ Subtotal  │ │
│  │  │ Product 1     │  │  │ Shipping  │ │
│  │  │ [- 1 +] [x]   │  │  │ Tax       │ │
│  │  └───────────────┘  │  │ ─────────  │ │
│  │                     │  │ Total     │ │
│  │  Or Payment Form    │  │ [Checkout]│ │
│  │  Email, Address,    │  │           │ │
│  │  Card, CVV...       │  │ (sticky)  │ │
│  │  [Place Order]      │  │           │ │
│  │                     │  └───────────┘ │
│  │  Success Screen     │                │
│  │  ✓ Confirmed!       │                │
│  │  [Back to Home]     │                │
│  │                     │                │
│  └─────────────────────┘                │
│                                          │
├──────────────────────────────────────────┤
│              FOOTER                      │
└──────────────────────────────────────────┘
```

---

## Technology Stack

```
┌─────────────────────────────────────────┐
│           Frontend Stack                 │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Vue 3 (Composition API)         │   │
│  │ - Component framework           │   │
│  │ - Reactive state                │   │
│  │ - Template syntax               │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Vite                            │   │
│  │ - Build tool                    │   │
│  │ - Dev server (HMR)              │   │
│  │ - Production bundler            │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Pinia                           │   │
│  │ - State management              │   │
│  │ - Stores (cart, product)        │   │
│  │ - Getters & actions             │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Vue Router                      │   │
│  │ - Client-side routing           │   │
│  │ - 3 pages (/, /product, /check) │   │
│  │ - Navigation links              │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Tailwind CSS                    │   │
│  │ - Utility-first CSS             │   │
│  │ - Dark theme                    │   │
│  │ - Responsive design             │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Lucide Vue Next                 │   │
│  │ - Icon library                  │   │
│  │ - Consistent icon set           │   │
│  │ - 24px default size             │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

---

## Build Process

```
Source Code (Vue/JS/CSS)
        │
        ▼
    Vite
    │
    ├─► Parse Vue components
    ├─► Compile templates
    ├─► Process Tailwind CSS
    ├─► Bundle JavaScript
    │
    ▼
  dist/
    ├─► index.html
    ├─► assets/
    │   ├─► main.js (bundled)
    │   └─► style.css (bundled)
    │
    ▼
  Ready for Production
    (Can be served on any static host)
```

---

## Browser Storage

```
localStorage
│
├─► axys-cart
│   └─► [
│         { id, name, price, quantity, image },
│         { id, name, price, quantity, image },
│         ...
│       ]
│
└─► Auto-synced by cart store
    on every change
```

---

## Responsive Breakpoints

```
Mobile (320px-767px)
├─► 1 column layouts
├─► Stacked sections
├─► Full-width buttons
└─► Compact spacing

        ▼

Tablet (768px-1023px)
├─► 2 column layouts
├─► Side-by-side sections
├─► Standard spacing
└─► Medium font sizes

        ▼

Desktop (1024px+)
├─► 2-3 column layouts
├─► Full width utilization
├─► Generous spacing
└─► Full-size fonts
```

---

**Last Updated**: 2025-12-20
**Version**: 1.0
