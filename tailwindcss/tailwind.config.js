/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../chatapp/templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'lato' : ['Lato', 'sans-serif']
      }
    },
  },
  plugins: [],
}

