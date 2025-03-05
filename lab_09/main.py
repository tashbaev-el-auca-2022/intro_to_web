x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(x / y)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    x = int("Hello")
except ValueError as e:
    print(f"Error: {e}")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"Error: {e}")

try:
    my_dict = {"key": "value"}
    print(my_dict["nonexistent"])
except KeyError as e:
    print(f"Error: {e}")

try:
    x = "Hello" + 5
except TypeError as e:
    print(f"Error: {e}")

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter integers.")

try:
    x = "hello" + 5
except (TypeError, ValueError) as e:
    print(f"Caught an error: {e}")

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Division was successful!")

try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
finally:
    print("This will run no matter what!")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount

try:
    print(withdraw(100, 150))
except ValueError as e:
    print(f"Error: {e}")

class NegativeNumberError(Exception):
    pass

def compute_square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot compute the square root of a negative number.")
    return x ** 0.5

try:
    print(compute_square_root(-4))
except NegativeNumberError as e:
    print(f"Error: {e}")

def divide(a, b):
    print(f"a = {a}, b = {b}")
    return a / b

print(divide(10, 2))

def check_positive(number):
    assert number > 0, "Number must be positive."
    print(f"{number} is positive.")

check_positive(10)
check_positive(-5)

try:
    result = 10 / 2
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Result:", result)
finally:
    print("Code executed.")

import logging

logging.basicConfig(level=logging.ERROR)
try:
    x = int("abc")
except ValueError as e:
    logging.error(f"Error: {e}")

import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

divide(10, 2)
