import os
import sys

import pytest


# Добавляем путь к src для импорта calculator
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from calculator import add, divide, multiply, subtract


class TestCalculator:
    """Тесты калькулятора для pytest"""

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(2.5, 3.5) == 6.0

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
        assert subtract(2.5, 1.5) == 1.0

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(2.5, 4) == 10.0

    def test_divide(self):
        assert divide(6, 3) == 2
        assert divide(5, 2) == 2.5
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(5, 0)
