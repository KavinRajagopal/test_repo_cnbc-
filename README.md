# Test Authoring Demo Repository

This is a sample Python project for testing the automated test generation tool.

## Setup

```bash
pip install -r requirements.txt
pytest
```

## Structure
- `src/` - Application code (calculator, user management, auth)
- `tests/` - Test files (generated tests will be added here)

## Features
- **Calculator** - Basic arithmetic operations with error handling
- **User Management** - User model with email and password validation
- **Authentication Service** - Registration, login, logout functionality

## Usage

```python
from src.calculator import Calculator
from src.auth import AuthService

# Calculator
calc = Calculator()
result = calc.divide(10, 2)  # Returns 5.0

# Authentication
auth = AuthService()
user = auth.register("user@example.com", "Password123")
user.activate()
token = auth.login("user@example.com", "Password123")
```

## Testing

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=src
```

## Test Generation

This repository is designed to work with the GitHub Test Authoring Tool. Create issues with acceptance criteria, and tests will be automatically generated!
