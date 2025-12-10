"""User management module."""
import re
from typing import Optional


class User:
    """User model with basic attributes."""
    
    def __init__(self, email: str, password: str, name: Optional[str] = None):
        """Initialize a user.
        
        Args:
            email: User email address
            password: User password (hashed in production)
            name: Optional display name
        """
        self.email = email
        self.password = password
        self.name = name or email.split('@')[0]
        self.is_active = False
        self.role = "user"
    
    def activate(self) -> None:
        """Activate user account."""
        self.is_active = True
    
    def deactivate(self) -> None:
        """Deactivate user account."""
        self.is_active = False
    
    def set_role(self, role: str) -> None:
        """Set user role.
        
        Args:
            role: Role to assign (user, admin, moderator)
            
        Raises:
            ValueError: If role is not valid
        """
        valid_roles = ["user", "admin", "moderator"]
        if role not in valid_roles:
            raise ValueError(f"Invalid role. Must be one of: {valid_roles}")
        self.role = role


def validate_email(email: str) -> bool:
    """Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid email format, False otherwise
    """
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_password(password: str) -> bool:
    """Validate password meets security requirements.
    
    Requirements:
    - At least 8 characters
    - At least one uppercase letter
    - At least one digit
    
    Args:
        password: Password to validate
        
    Returns:
        True if valid, False otherwise
    """
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

