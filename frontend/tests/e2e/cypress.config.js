const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'http://localhost:3000', // Replace with your application's URL
    specPattern: 'tests/e2e/specs/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'tests/e2e/support/e2e.js',
    video: false, // Set to true to record videos of tests
    screenshotOnRunFailure: true,
    viewportHeight: 1080,
    viewportWidth: 1920,
    chromeWebSecurity: false //Disable same-origin policy for local development
  },
  
  component: {
    devServer: {
      framework: 'react', // or other framework
      bundler: 'webpack' // or other bundler
    }
  }
})
