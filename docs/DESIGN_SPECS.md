# AXYS Golf Cleaner - Design Specifications

## Brand Identity

### Logo
- **AXYS Logo**: Silver/metallic water drop with text
- **Tagline**: "Precision Clean. Flawless Play."
- **Style**: Minimalist, premium, modern

### Product Image
- **AXYS Premium Golf Cleaner**: Black cylindrical container with golf cart mount
- **Setting**: Golf course (green background)
- **Highlights**: Metallic finish, mounting bracket, premium construction

---

## Color Palette

### Dark Theme (Primary)
```
Primary Background:    #0f0f0f (rgb(15, 15, 15))
Secondary Background:  #1a1a1a (rgb(26, 26, 26))
Tertiary Background:   #2a2a2a (rgb(42, 42, 42))

Text Primary:          #ffffff (White)
Text Secondary:        #a0a0a0 (Gray-400)
Text Tertiary:         #707070 (Gray-500)

Border:                #2a2a2a (Gray-800)
Border Hover:          #3a3a3a (Gray-700)

Accent (Primary):      #ffffff (White)
Success:               #10b981 (Green-500)
Error:                 #ef4444 (Red-500)
Warning:               #f59e0b (Amber-500)

Gradient Overlay:      rgba(26, 26, 26, 0.9) to rgba(0, 0, 0, 1)
```

### Typography

#### Font Family
- **Primary**: System fonts (-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif)
- **Fallback**: Arial, sans-serif

#### Font Sizes
```
Hero Title (H1):       48px (mobile) / 56px (tablet) / 64px (desktop)
Section Title (H2):    36px (mobile) / 40px (tablet) / 48px (desktop)
Subheading (H3):       24px (mobile) / 28px (tablet) / 32px (desktop)
Body Large:            18px / 20px line-height
Body Regular:          16px / 24px line-height
Body Small:            14px / 20px line-height
Caption:               12px / 16px line-height
```

#### Font Weights
```
Regular:   400
Medium:    500
Semibold:  600
Bold:      700
```

#### Line Heights
```
Tight:     1.2
Normal:    1.5
Relaxed:   1.75
Loose:     2
```

---

## Component Styling

### Buttons

#### Primary Button
```
Background:     #ffffff (white)
Text Color:     #0f0f0f (black)
Padding:        12px 32px (py-3 px-8)
Border:         None
Border Radius:  0px (squared edges)
Font Size:      16px
Font Weight:    500
Cursor:         pointer

Hover State:
  Background:   #e5e5e5 (gray-200)
  Transition:   200ms ease-in-out

Active State:
  Background:   #cccccc (gray-300)
```

#### Secondary Button
```
Background:     transparent
Text Color:     #ffffff (white)
Padding:        12px 32px
Border:         1px solid #ffffff
Border Radius:  0px
Font Size:      16px
Font Weight:    500

Hover State:
  Background:   #ffffff
  Text Color:   #0f0f0f
  Transition:   200ms ease-in-out
```

#### Small Button (Quantity Controls)
```
Width:          40px
Height:         40px
Background:     transparent
Border:         1px solid #2a2a2a
Text Color:     #ffffff
Border Radius:  0px
Font Weight:    500

Hover State:
  Background:   #1a1a1a
  Border Color: #3a3a3a
```

### Cards

#### Feature Card
```
Background:     #1a1a1a
Border:         1px solid #2a2a2a
Padding:        32px
Border Radius:  0px
Box Shadow:     None

Hover State:
  Border Color: #3a3a3a
  Transition:   200ms ease-in-out
```

#### Product Card (Checkout)
```
Background:     #0f0f0f
Border:         1px solid #2a2a2a
Padding:        24px
Display:        flex gap-24px
Border Radius:  0px

Image Size:     96px × 96px
Image BG:       #1a1a1a
```

### Input Fields

#### Text Input
```
Background:     #1a1a1a
Border:         1px solid #2a2a2a
Text Color:     #ffffff
Padding:        12px 16px
Border Radius:  0px
Font Size:      16px

Focus State:
  Border Color: #ffffff
  Outline:      none
  Transition:   200ms ease-in-out

Placeholder:
  Color:        #707070
```

### Icons

#### Icon Styling
- **Library**: lucide-vue-next
- **Size**: 24px (default), 20px (small), 32px (large)
- **Color**: Inherit from context (white in dark areas)
- **Stroke Width**: 2px

---

## Layout & Spacing

### Container
```
Max Width:      1024px (md) / 1280px (lg)
Horizontal Padding:
  Mobile:       16px
  Tablet:       24px
  Desktop:      24px
```

### Spacing Scale
```
4px:   1
8px:   2
12px:  3
16px:  4
20px:  5
24px:  6
32px:  8
40px:  10
48px:  12
64px:  16
```

### Section Padding
```
Top/Bottom:
  Mobile:       64px (py-16)
  Desktop:      96px (py-24)
```

### Gap (Between Items)
```
Columns:        32px
Rows:           32px
Items in Row:   16px
```

---

## Responsive Breakpoints

```
Mobile:   320px - 767px
Tablet:   768px - 1023px
Desktop:  1024px+

Grid Behavior:
  Mobile:   1 column
  Tablet:   2 columns
  Desktop:  2-3 columns (varies by section)
```

---

## Page Layouts

### Landing Page

#### Hero Section
```
Layout:         2-column grid (mobile: 1 col, stacked)
Height:         600px-800px
Background:     Gradient overlay + dark
Text Side:
  - H1 (64px)
  - Description (18px)
  - 2 CTA buttons side-by-side (mobile: stacked)
Image Side:
  - Product image (full width)
  - Drop shadow effect
```

#### Features Section
```
Background:     #0f0f0f
Padding:        96px horizontal, 96px vertical
Title (H2):     Centered, 48px, white
Cards Grid:     3 columns (mobile: 1, tablet: 2)
Card Spacing:   32px
```

#### CTA Section
```
Background:     Gradient (#2a2a2a to #1a1a1a)
Padding:        64px horizontal, 96px vertical
Border:         1px solid #2a2a2a
Title (H2):     48px, centered, white
Text:           18px, centered, gray-400
Button:         Centered, primary style
```

### Product Page

#### Product Grid
```
Layout:         2 columns (mobile: 1, tablet: 1)
Gap:            96px
Max Width:      1280px

Left Column (Image):
  Background:   Gradient overlay
  Padding:      48px
  Height:       500px-600px
  Display:      flex, center items
  
Right Column (Info):
  Padding:      0
  Display:      flex flex-col
  Justify:      center
```

#### Product Info Section
```
Rating:         5 stars + review count (16px gray)
Title (H1):     56px white
Price (H2):     36px white
Description:    18px gray-400
Features List:  16px gray-300 with checkmarks
Spacing:        24px between sections
```

#### Specifications Grid
```
Background:     #0f0f0f
Border:         1px solid #2a2a2a
Padding:        32px
Grid:           2 columns (mobile: 1)
Gap:            24px
```

### Checkout Page

#### Layout
```
Max Width:      1280px
Grid:           3 columns (mobile: 1, tablet: 1)
Columns:
  1-2: Cart/Form (2/3 width)
  3:   Summary (1/3 width, sticky)
Gap:            32px
```

#### Cart Item Card
```
Layout:         flex row
Image:          96px × 96px, bg #1a1a1a
Content:        flex-1, padding 24px
Actions:        right side, delete + price
```

#### Order Summary
```
Background:     #0f0f0f
Border:         1px solid #2a2a2a
Padding:        24px
Sticky:         top-24px (sticky positioning)
Border Radius:  0px
```

---

## Effects & Animations

### Transitions
```
Default:        200ms ease-in-out
Button Hover:   200ms ease-in-out
Card Hover:     200ms ease-in-out
Input Focus:    200ms ease-in-out
```

### Hover Effects
```
Buttons:
  - Background/Text color change
  - Smooth transition 200ms

Cards:
  - Border color change to lighter gray
  - Subtle shadow or opacity

Links:
  - Color change to white
  - Underline on hover (optional)
```

### Drop Shadow
```
Product Image:  filter drop-shadow-2xl (strong shadow)
Success Icon:   No shadow
Cards:          No shadow (use borders instead)
```

---

## Image Specifications

### Product Image
- **File**: `product.png` (or JPEG)
- **Dimensions**: 800px × 800px (flexible, square ratio preferred)
- **Format**: PNG with transparency preferred
- **Use**: Hero section, Product page, Checkout

### Logo Image
- **File**: `logo.png`
- **Dimensions**: Flexible (100px height in header)
- **Format**: PNG with transparency
- **Use**: Header, Footer

### Icon Assets
- **Library**: lucide-vue-next (recommended)
- **Fallback**: SVG files if needed
- **Colors**: Inherit from parent (use currentColor)

---

## Accessibility

### Color Contrast
```
Primary Text (#ffffff) on Dark (#0f0f0f):   21:1 ✓ AAA
Secondary Text (#a0a0a0) on Dark (#0f0f0f): 7.5:1 ✓ AA
```

### Focus States
```
All interactive elements:
  - Visible focus ring
  - High contrast border or outline
  - Not removed with CSS (outline: none forbidden)
```

### Typography
```
Minimum Font Size:    14px
Line Height Minimum:  1.5
Letter Spacing:       Normal (0px)
```

### Touch Targets
```
Minimum Size:   44px × 44px
Padding Around: 8px minimum
```

---

## Dark Mode Implementation

The entire site uses a dark theme by default. No light mode toggle is needed.

### Tailwind CSS Configuration
```javascript
theme: {
  colors: {
    dark: {
      900: '#0f0f0f',  // Primary background
      800: '#1a1a1a',  // Secondary background
      700: '#2a2a2a',  // Borders/dividers
      600: '#3a3a3a',  // Hover states
    },
    gray: {
      400: '#a0a0a0',  // Secondary text
      500: '#707070',  // Tertiary text
    }
  }
}
```

---

## Performance Considerations

### Image Optimization
- Use WebP format where possible
- Implement lazy loading
- Compress images before upload
- Use appropriate dimensions

### CSS & JavaScript
- Minify in production builds
- Remove unused Tailwind classes
- Code-split pages (lazy load routes)
- Defer non-critical JavaScript

### Responsive Images
```html
<img
  src="product.png"
  alt="AXYS Product"
  loading="lazy"
  class="w-full h-auto"
/>
```

---

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

---

**Last Updated:** 2025-12-20
