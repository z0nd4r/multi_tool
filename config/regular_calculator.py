import numexpr
import numpy as np

def calculation(text):
    result = float(numexpr.evaluate(text))

    if result.is_integer():
        return int(result)
    else:
        return f"{result:.2f}"