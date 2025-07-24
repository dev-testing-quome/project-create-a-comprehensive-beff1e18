This directory contains comprehensive tests for **{project.name}**.

## Test Structure

```
tests/
├── unit/                    # Unit tests
│   ├── frontend/           # React component tests
│   └── backend/            # Python function tests
├── integration/            # Integration tests
│   ├── api/               # API endpoint tests
│   └── database/          # Database tests
├── e2e/                   # End-to-end tests
│   ├── specs/            # Cypress test specs
│   └── fixtures/         # Test data
└── setup/                 # Test configuration
```

## Test Categories

### 🔬 Unit Tests
- **Frontend**: Component rendering, hooks, utilities
- **Backend**: API functions, business logic, models
- **Coverage Target**: 80%+

### 🔗 Integration Tests  
- **API Integration**: Full request/response cycles
- **Database Integration**: CRUD operations with real DB
- **Frontend-Backend**: End-to-end data flow

### 🎭 E2E Tests
- **User Journeys**: Complete application workflows
- **Cross-browser**: Chrome, Firefox, Safari testing
- **Mobile Responsive**: Mobile device testing

## Running Tests

### All Tests
```bash
# Run complete test suite
npm run test:all

# Run with coverage
npm run test:coverage
```

### Unit Tests
```bash
# Frontend unit tests
npm test

# Backend unit tests  
pytest tests/unit/backend/

# Watch mode
npm test -- --watch
```

### Integration Tests
```bash
# API integration tests
pytest tests/integration/

# Frontend integration tests
npm run test:integration
```

### E2E Tests
```bash
# Headless mode
npm run test:e2e

# Interactive mode
npm run test:e2e:open

# Specific browser
npm run test:e2e:chrome
```

## Test Configuration

### Coverage Requirements
- **Minimum Coverage**: 80%
- **Branch Coverage**: 80%
- **Function Coverage**: 80%

### Test Data
- **Fixtures**: Located in `tests/fixtures/`
- **Factories**: Using Factory Boy for Python, MSW for JavaScript
- **Mocks**: API mocking with appropriate libraries

### CI/CD Integration
- **GitHub Actions**: Automated test runs on push/PR
- **Coverage Reports**: Uploaded to Codecov
- **Quality Gates**: Tests must pass for merge

## Writing Tests

### Frontend Testing (Jest + RTL)
```typescript
import {{ render, screen, fireEvent }} from '@testing-library/react';
import MyComponent from '../MyComponent';

describe('MyComponent', () => {{
  it('renders correctly', () => {{
    render(<MyComponent />);
    expect(screen.getByText('Hello')).toBeInTheDocument();
  }});
}});
```

### Backend Testing (pytest)
```python
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_api_endpoint(client):
    response = client.get("/api/users")
    assert response.status_code == 200
```

### E2E Testing (Cypress)
```javascript
describe('User Journey', () => {{
  it('completes registration flow', () => {{
    cy.visit('/register');
    cy.get('[data-testid="email"]').type('user@example.com');
    cy.get('[data-testid="submit"]').click();
    cy.url().should('include', '/dashboard');
  }});
}});
```

## Test Files Generated

{test_file_paths_formatted}

## Maintenance

### Adding New Tests
1. **Unit Tests**: Add alongside new components/functions
2. **Integration Tests**: Add for new API endpoints  
3. **E2E Tests**: Add for new user journeys

### Updating Tests
- Keep tests updated with code changes
- Maintain test data and fixtures
- Update coverage thresholds as needed

### Debugging Tests
- Use `--verbose` flag for detailed output
- Check coverage reports for missed areas
- Use browser dev tools for E2E debugging