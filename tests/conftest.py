"""Pytest configuration and shared fixtures."""
import pytest
from src.auth import AuthService
from src.calculator import Calculator


@pytest.fixture
def calculator():
    """Create calculator instance."""
    return Calculator()


@pytest.fixture
def auth_service():
    """Create auth service instance."""
    return AuthService()


@pytest.fixture
def sample_user(auth_service):
    """Create and return a sample activated user."""
    user = auth_service.register("test@example.com", "Password123", "Test User")
    user.activate()
    return user


@pytest.fixture
def logged_in_user(auth_service, sample_user):
    """Create logged in user with session token."""
    token = auth_service.login("test@example.com", "Password123")
    return {"user": sample_user, "token": token}

