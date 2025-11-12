import os
import sys


# Добавляем путь к src для импорта calculator
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from calculator import add, divide, multiply, subtract


def test_add():
    """Тест функции сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("✅ Все тесты сложения пройдены")


def test_subtract():
    """Тест функции вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    print("✅ Все тесты вычитания пройдены")


def test_multiply():
    """Тест функции умножения"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    print("✅ Все тесты умножения пройдены")


def test_divide():
    """Тест функции деления"""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0
    print("✅ Все тесты деления пройдены")


def test_divide_by_zero():
    """Тест деления на ноль"""
    try:
        divide(5, 0)
        assert False, "Должна быть ошибка деления на ноль"
    except ValueError:
        print("✅ Тест деления на ноль пройден")


def run_all_tests():
    """Запуск всех тестов"""
    print("🧪 ЗАПУСК ТЕСТОВ")
    print("=" * 30)

    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()

    print("=" * 30)
    print("🎉 Все тесты успешно пройдены!")


if __name__ == "__main__":
    run_all_tests()
