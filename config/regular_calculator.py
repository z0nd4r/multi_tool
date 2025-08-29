import numexpr
from tkinter import messagebox
import numpy as np


def calculation(text, max_digits=0):
    MAX_INT64 = 2 ** 63 - 1  # 9,223,372,036,854,775,807
    MIN_INT64 = -2 ** 63  # -9,223,372,036,854,775,808

    """
    Вычисляет математическое выражение с интеллектуальным форматированием
    """
    try:
        # вычисляем выражение
        result = float(numexpr.evaluate(text))
        print(result)

        # определяем абсолютное значение для выбора формата
        abs_val = abs(result)
        print(abs_val)

        # выбор формата вывода
        if abs_val >= 1e6 or (0 < abs_val <= 1e-4):
            return f"{result:.{max_digits}e}"  # экспоненциальная запись
        else:
            # return f"{result:.{max_digits}g}"  # умный формат
            if result.is_integer():
                try:
                    return int(result)
                except OverflowError:
                    return str(int(result))
            else:
                return f'{result:.2f}'

    except (ValueError, SyntaxError):
        messagebox.showerror("Ошибка", "Неверное выражение")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль")
    except Exception as e:
        messagebox.showerror("Ошибка", f"{str(e)}")