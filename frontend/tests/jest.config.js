
module.exports = {
  preset: '@testing-library/jest-dom',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/tests/setup/jest.setup.js'],
  testMatch: [
    '<rootDir>/tests/unit/frontend/**/*.test.{js,jsx,ts,tsx}',
    '<rootDir>/tests/integration/frontend/**/*.test.{js,jsx,ts,tsx}'
  ],
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/index.tsx'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  transform: {
    '^.+\.(ts|tsx)$': 'ts-jest'
  }
};
