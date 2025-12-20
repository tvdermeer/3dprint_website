# Frontend Component Documentation

## Components

### Header.vue
**Path**: `src/components/Header.vue`
**Purpose**: Displays the global navigation bar, branding, and shopping cart indicator.

- **Features**:
  - Responsive design (different layouts for mobile/desktop).
  - Shows "AXYS" logo linking to Home.
  - Navigation links to Home and Product pages.
  - Cart icon with a dynamic badge showing total items.
- **Dependencies**:
  - `vue-router`: For navigation links.
  - `pinia` (`useCartStore`): To get the total item count for the badge.
  - `lucide-vue-next`: For the ShoppingCart icon.

### Footer.vue
**Path**: `src/components/Footer.vue`
**Purpose**: Displays the site footer with links and contact info.

- **Features**:
  - Links to pages (Home, Product, Checkout).
  - Support contact information (mock).
  - Dynamic copyright year.
- **Dependencies**:
  - `vue-router`: For navigation links.

### ProductCard.vue (Planned)
*Note: Currently integrated directly into LandingPage.vue, but can be extracted for scalability.*

## Views (Pages)

### LandingPage.vue
**Path**: `src/views/LandingPage.vue`
**Route**: `/`
**Purpose**: The main entry point, marketing the product.

- **Sections**:
  - **Hero**: Large image and value proposition with "Shop Now" CTA.
  - **Features**: Grid of 3 key selling points (Premium Formula, Durable Design, Perfect Results).
  - **CTA**: Final call to action to order.
- **Dependencies**:
  - `lucide-vue-next`: Icons for features.

### ProductPage.vue
**Path**: `src/views/ProductPage.vue`
**Route**: `/product`
**Purpose**: Detailed product view allowing users to add to cart.

- **Features**:
  - Fetches product data from Backend API on mount.
  - Displays product details (name, price, description).
  - Quantity selector (+/-).
  - "Add to Cart" button (integrates with Cart Store).
  - Trust badges (Shipping, Warranty).
- **State**:
  - Uses `useProductStore` to fetch and store product data.
  - Uses `useCartStore` to add items.

### CheckoutPage.vue
**Path**: `src/views/CheckoutPage.vue`
**Route**: `/checkout`
**Purpose**: Manages the shopping cart and order submission.

- **Features**:
  - **Cart View**: Lists items, allows quantity adjustment or removal. Shows financial summary.
  - **Payment View**: Collects customer details (shipping/payment). *Note: Payment form is currently a mockup.*
  - **Success View**: Confirmation message after order submission.
- **Integration**:
  - Submits order to Backend API (`POST /api/v1/orders`).
  - Clears cart on successful order.
  - Validates basic form fields.

---

# State Management (Pinia)

## Cart Store
**Path**: `src/stores/cart.js`
**Id**: `cart`

### State
- `items`: Array of product objects with `quantity`.

### Getters
- `totalItems`: Total count of individual units in cart.
- `totalPrice`: Total monetary value of cart.
- `cartItems`: Returns the items array.

### Actions
- `addToCart(item, quantity)`: Adds item or increments existing quantity.
- `removeFromCart(itemId)`: Removes item by ID.
- `updateQuantity(itemId, quantity)`: Sets specific quantity (removes if <= 0).
- `clearCart()`: Empties cart.
- `saveToLocalStorage()`: Persists state.
- `loadFromLocalStorage()`: Hydrates state.

## Product Store
**Path**: `src/stores/product.js`
**Id**: `product`

### State
- `products`: Array of loaded products.
- `currentProduct`: Currently selected product details.
- `loading`: Boolean status of API requests.
- `error`: Error message string or null.

### Actions
- `fetchProducts()`: Gets list from API.
- `fetchProductById(id)`: Gets single product detail.

---

# Environment Configuration

The frontend requires the following environment variables (in `.env` or `.env.local`):

```ini
# URL of the Backend API (e.g., FastAPI server)
VITE_API_BASE_URL=http://localhost:8000/api/v1
```
