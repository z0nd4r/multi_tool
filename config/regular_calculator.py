import numexpr
from tkinter import messagebox
import numpy as np


def calculation(text, max_digits=6):
    MAX_INT64 = 2 ** 63 - 1  # 9,223,372,036,854,775,807
    MIN_INT64 = -2 ** 63  # -9,223,372,036,854,775,808

    """
    Вычисляет математическое выражение с интеллектуальным форматированием
    """
    try:
        # Вычисляем выражение
        result = float(numexpr.evaluate(text))
        print(result)

        # Обрабатываем специальные случаи
        if result.is_integer():
            try:
                return int(result)
            except OverflowError:
                return str(int(result))

        # Определяем абсолютное значение для выбора формата
        abs_val = abs(result)
        print(abs_val)

        # Автоматический выбор формата вывода
        if abs_val >= 1e6 or (0 < abs_val <= 1e-4):
            return f"{result:.{max_digits - 1}e}"  # Экспоненциальная запись
        else:
            # return f"{result:.{max_digits}g}"  # Умный формат
            if result.is_integer():
                try:
                    return int(result)
                except OverflowError:
                    return str(int(result))

    except (ValueError, SyntaxError):
        messagebox.showerror("Ошибка", "Неверное выражение")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль")
    except Exception as e:
        messagebox.showerror("Ошибка", f"{str(e)}")