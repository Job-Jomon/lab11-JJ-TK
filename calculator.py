"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Square root is not defined for negative numbers.")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Invalid input type. Expected a number.")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Invalid input types. Expected numbers.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid arguments for logarithm. Base must be > 0 and != 1; value must be > 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b