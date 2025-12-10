"""Authentication module."""
from typing import Optional, Dict
from src.user import User, validate_email, validate_password


class AuthenticationError(Exception):
    """Authentication failed."""
    pass


class AuthService:
    """Handle user authentication and session management."""
    
    def __init__(self):
        """Initialize auth service with empty storage."""
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, User] = {}
    
    def register(self, email: str, password: str, name: Optional[str] = None) -> User:
        """Register a new user.
        
        Args:
            email: User email
            password: User password
            name: Optional display name
            
        Returns:
            Created user object
            
        Raises:
            ValueError: If validation fails or email exists
        """
        if not validate_email(email):
            raise ValueError("Invalid email format")
        
        if not validate_password(password):
            raise ValueError(
                "Password must be at least 8 characters with uppercase and digit"
            )
        
        if email in self.users:
            raise ValueError("Email already registered")
        
        user = User(email, password, name)
        self.users[email] = user
        return user
    
    def login(self, email: str, password: str) -> str:
        """Login user and return session token.
        
        Args:
            email: User email
            password: User password
            
        Returns:
            Session token
            
        Raises:
            AuthenticationError: If credentials invalid or account inactive
        """
        user = self.users.get(email)
        
        if not user:
            raise AuthenticationError("Invalid credentials")
        
        if user.password != password:
            raise AuthenticationError("Invalid credentials")
        
        if not user.is_active:
            raise AuthenticationError("Account not activated")
        
        # Generate simple session token (use secure token in production)
        session_token = f"session_{email}_{hash(password)}"
        self.sessions[session_token] = user
        return session_token
    
    def logout(self, session_token: str) -> None:
        """Logout user by removing session.
        
        Args:
            session_token: Token to invalidate
        """
        if session_token in self.sessions:
            del self.sessions[session_token]
    
    def get_user_by_token(self, session_token: str) -> Optional[User]:
        """Get user associated with session token.
        
        Args:
            session_token: Session token
            
        Returns:
            User object if valid token, None otherwise
        """
        return self.sessions.get(session_token)

