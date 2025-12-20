# AXYS Frontend - Quick Reference Card

## 📋 9 Phases at a Glance

| Phase | Name | Duration | Key Files | Status |
|-------|------|----------|-----------|--------|
| 1 | Setup & Config | 2-3h | vite.config.js, tailwind.config.js, router/index.js | ⏳ |
| 2 | Components | 2-3h | Header.vue, Footer.vue, App.vue | ⏳ |
| 3 | State Mgmt | 1-2h | stores/cart.js | ⏳ |
| 4 | Landing Page | 2-3h | views/LandingPage.vue | ⏳ |
| 5 | Product Page | 3-4h | views/ProductPage.vue + QuantitySelector.vue | ⏳ |
| 6 | Checkout | 3-4h | views/CheckoutPage.vue | ⏳ |
| 7 | Styling | 2-3h | globals.css + component tweaks | ⏳ |
| 8 | Testing | 2-3h | Manual testing & fixes | ⏳ |
| 9 | Docs | 1-2h | README.md + code comments | ⏳ |

**Total: 18-25 hours | ~3,000-4,000 LOC | ~20-25 files**

---

## 🎨 Design Tokens

### Colors
```css
--bg-primary:     #0f0f0f  /* Main background */
--bg-secondary:   #1a1a1a  /* Card background */
--border:         #2a2a2a  /* Borders */
--text-primary:   #ffffff  /* Main text */
--text-secondary: #a0a0a0  /* Secondary text */
--success:        #10b981  /* Green success */
```

### Typography
```
H1: 64px (desktop) / 48px (mobile)
H2: 48px (desktop) / 36px (mobile)
H3: 32px (desktop) / 24px (mobile)
Body: 16px (line-height: 1.5)
Small: 14px
```

### Spacing
```
xs: 8px    sm: 16px   md: 24px   lg: 32px   xl: 48px   2xl: 64px
```

---

## 🔧 Key Dependencies

```json
{
  "vue": "^3.3.0",
  "vue-router": "^4.2.0",
  "pinia": "^2.1.0",
  "tailwindcss": "^3.3.0",
  "lucide-vue-next": "^0.263.0"
}
```

---

## 📁 Folder Structure

```
frontend/src/
├── components/          # Reusable components
│   ├── Header.vue
│   ├── Footer.vue
│   └── QuantitySelector.vue
├── views/               # Page components
│   ├── LandingPage.vue
│   ├── ProductPage.vue
│   └── CheckoutPage.vue
├── stores/              # Pinia stores
│   └── cart.js
├── router/              # Vue Router config
│   └── index.js
├── assets/
│   ├── images/          # Product images
│   │   ├── product.png
│   │   └── logo.png
│   └── css/
│       └── globals.css
├── App.vue              # Root component
└── main.js              # Entry point
```

---

## 🛒 Cart Store API

```javascript
// Composable usage
import { useCartStore } from '@/stores/cart'

const cart = useCartStore()

// Add item
cart.addToCart({ id, name, price, image })

// Remove item
cart.removeFromCart(id)

// Update quantity
cart.updateQuantity(id, quantity)

// Clear all
cart.clearCart()

// Getters
cart.totalItems      // Number of items
cart.totalPrice      // Total price ($)
cart.items           // Cart items array
```

---

## 🔗 Routes

```javascript
/                 → LandingPage (home)
/product          → ProductPage (product details)
/checkout         → CheckoutPage (cart + payment)
```

---

## 📱 Responsive Breakpoints

```css
Mobile:   320px - 767px   (1 column, stacked)
Tablet:   768px - 1023px  (2 columns)
Desktop:  1024px+         (2-3 columns)
```

---

## 💰 Pricing Calculations

```javascript
subtotal = sum(price × quantity)
shipping = 9.99 (if items)
tax = subtotal × 0.08
total = subtotal + shipping + tax
```

---

## ✨ Component Checklist

### Header
- [ ] Logo (left)
- [ ] Nav links (center)
- [ ] Cart icon with badge (right)
- [ ] Sticky positioning
- [ ] Responsive nav (hide on mobile)

### Landing Page
- [ ] Hero: headline + CTA buttons + image
- [ ] Features: 3 cards with icons
- [ ] CTA: "Elevate Your Game" section
- [ ] Responsive grid (1/2/3 columns)

### Product Page
- [ ] 2-column layout (image / info)
- [ ] Rating & reviews
- [ ] Features checklist
- [ ] Quantity selector
- [ ] Add to cart button
- [ ] Trust badges (3 items)
- [ ] Specifications table

### Checkout Page
- [ ] Multi-step: cart → payment → success
- [ ] Product list with controls
- [ ] Order summary (sticky)
- [ ] Payment form with validation
- [ ] Success screen
- [ ] Empty cart state

---

## 🎯 Key Features

✅ Dark theme throughout (#0f0f0f)
✅ Responsive design (mobile-first)
✅ Shopping cart with persistence
✅ Multi-step checkout flow
✅ Form validation
✅ Success confirmation
✅ Smooth transitions (200ms)
✅ No rounded corners (squared design)
✅ Accessible (WCAG AA)
✅ Fast (Vite + optimized images)

---

## 📊 Product Data

```javascript
{
  id: 'axys-cleaner-1',
  name: 'AXYS Premium Golf Cleaner',
  price: 39.99,
  rating: 5,
  reviews: 247,
  description: 'The ultimate golf club cleaning solution...',
  features: [
    'Premium cleaning formula',
    'Durable metallic construction',
    'Universal cart mount included',
    'Weather-resistant design'
  ],
  specs: {
    dimensions: '4.5" H × 3.2" W',
    material: 'Powder-coated aluminum',
    capacity: '12 oz',
    mounting: 'Universal cart bracket'
  }
}
```

---

## 🧪 Test Scenarios

### Cart Tests
- [ ] Add item → count badge shows
- [ ] Remove item → count updates
- [ ] Update quantity → total updates
- [ ] Refresh page → cart persists
- [ ] Clear cart → empty state

### Checkout Tests
- [ ] Cart → Payment → Success
- [ ] Form validation
- [ ] Tax calculation (8%)
- [ ] Shipping ($9.99)
- [ ] Success auto-clears cart

### Responsive Tests
- [ ] Mobile (375px) - single column
- [ ] Tablet (768px) - two columns
- [ ] Desktop (1440px) - full layout
- [ ] Images scale properly
- [ ] Touch targets ≥44px

### Navigation Tests
- [ ] All links work
- [ ] Router transitions smooth
- [ ] Back buttons function
- [ ] Cart badge updates

---

## 🚀 Commands

```bash
# Development
npm run dev           # Start dev server (port 5173)
npm run build         # Build for production
npm run preview       # Preview production build

# Quality
npm run lint          # Run ESLint
npm run type-check    # Type checking (if added)

# Advanced
npm run dev -- --host           # Access from other machines
npm run build -- --sourcemap    # Build with source maps
```

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| **IMPLEMENTATION_GUIDE.md** | Detailed phase-by-phase instructions |
| **DESIGN_SPECS.md** | Complete styling guide |
| **WORK_LOG.md** | Progress tracking |
| **IMPLEMENTATION_SUMMARY.md** | Project overview |
| **QUICK_REFERENCE.md** | This file (quick lookup) |

---

## 🔍 Quick Lookup

**"How do I create a component?"**
→ See Phase 2 in IMPLEMENTATION_GUIDE.md

**"What's the button styling?"**
→ See Component Styling in DESIGN_SPECS.md

**"What files have I created?"**
→ See WORK_LOG.md

**"What's the whole project about?"**
→ See IMPLEMENTATION_SUMMARY.md

**"What's the status?"**
→ See Phase breakdown table above

---

## ⚡ Pro Tips

1. **Use Tailwind for everything** - don't write custom CSS except globals
2. **Dark theme by default** - no light mode needed
3. **Component composition** - break into small, reusable pieces
4. **localStorage magic** - cart store auto-persists to localStorage
5. **Router simplicity** - just 3 routes, no nesting
6. **Test early, test often** - manual testing at each phase
7. **Images matter** - product image is hero of the site
8. **Responsive first** - test mobile (375px) first

---

**Last Updated**: 2025-12-20
**Ready to start Phase 1?** See IMPLEMENTATION_GUIDE.md
