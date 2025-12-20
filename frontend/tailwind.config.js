/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        white: '#ffffff',
        // Dark theme colors (primary palette)
        dark: {
          900: '#0f0f0f', // Primary background
          800: '#1a1a1a', // Secondary background
          700: '#2a2a2a', // Borders
          600: '#3a3a3a', // Hover states
        },
        gray: {
          200: '#e5e5e5',
          400: '#a0a0a0', // Secondary text
          500: '#707070', // Tertiary text
        },
      },
      backgroundColor: {
        'primary': '#0f0f0f',
        'secondary': '#1a1a1a',
        'dark-900': '#0f0f0f',
        'dark-800': '#1a1a1a',
        'dark-700': '#2a2a2a',
        'dark-600': '#3a3a3a',
      },
      textColor: {
        primary: '#ffffff',
        secondary: '#a0a0a0',
      },
      borderColor: {
        DEFAULT: '#2a2a2a',
      },
      container: {
        center: true,
        padding: '1rem',
      },
      fontFamily: {
        sans: [
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          'sans-serif',
        ],
      },
    },
  },
  plugins: [],
}
