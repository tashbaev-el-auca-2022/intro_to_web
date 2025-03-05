def square(n):
    return n * n

print(square(4))

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4]))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
