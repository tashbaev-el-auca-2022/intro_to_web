def greet():
    print("Hello, world!")

greet()

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def greet(name="Elmurat"):
    print(f"Hello, {name}!")

greet("Armin")
greet()

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([1, 2, 3, 4, 5])
print(result)

def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Mikasa", age=25)

add_numbers = lambda x, y: x + y
print(add_numbers(3, 4))

numbers = [(1, 'one'), (3, 'three'), (2, 'two')]
numbers.sort(key=lambda x: x[0])
print(numbers)

def local_example():
    a = 10
    print(a)

a = 10

def global_example():
    global a
    a = 20
    print(a)

global_example()
print(a)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def greet(name):
    """
    This function takes a name and prints a greeting message.
    :param name: Name of the person to greet
    """
    print(f"Hello, {name}!")

print(greet.__doc__)
