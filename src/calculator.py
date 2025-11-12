def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность a - b"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Возвращает произведение"""
    return a * b


def divide(a: float, b: float) -> float:
    """Возвращает результат деления a / b, если b ≠ 0"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return a / b


def calculator():
    """Интерактивный калькулятор"""
    print("🧮 КАЛЬКУЛЯТОР")
    print("=" * 30)

    while True:
        try:
            print("\nДоступные операции: +, -, *, /")
            print("Введите 'exit' для выхода")

            a = input("Введите первое число: ")
            if a.lower() == "exit":
                break

            operation = input("Введите операцию (+, -, *, /): ")
            if operation.lower() == "exit":
                break

            b = input("Введите второе число: ")
            if b.lower() == "exit":
                break

            a = float(a)
            b = float(b)

            if operation == "+":
                result = add(a, b)
            elif operation == "-":
                result = subtract(a, b)
            elif operation == "*":
                result = multiply(a, b)
            elif operation == "/":
                result = divide(a, b)
            else:
                print("❌ Неизвестная операция")
                continue

            print(f"✅ Результат: {a} {operation} {b} = {result}")

        except ValueError as e:
            print(f"❌ Ошибка ввода: {e}")
        except ZeroDivisionError:
            print("❌ Ошибка: Деление на ноль!")
        except KeyboardInterrupt:
            print("\n👋 До свидания!")
            break


if __name__ == "__main__":
    calculator()
