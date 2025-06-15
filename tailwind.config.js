/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./realtime_transcription/templates/**/*.html"], 
  theme: {
    extend: {
      fontFamily: {
        rampartOne: ["Rampart One", "sans-serif"],
        kosugiMaru: ["Kosugi Maru", "sans-serif"],
      },
    },
  },
  plugins: [],
}


