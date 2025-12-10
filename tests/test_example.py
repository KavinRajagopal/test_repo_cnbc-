"""Example test file showing patterns for AI to learn from."""
import pytest
from src.calculator import Calculator


class TestCalculatorBasics:
    """Basic calculator tests as examples."""
    
    def test_addition(self, calculator):
        """Test basic addition."""
        result = calculator.add(2, 3)
        assert result == 5
    
    def test_subtraction(self, calculator):
        """Test basic subtraction."""
        result = calculator.subtract(10, 4)
        assert result == 6
    
    def test_division_by_zero_raises_error(self, calculator):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)

