import math

num1 = 15
num2 = 8

print("Elmurat:")
print("")

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
print("Remainder:", num1 % num2)
print("Floor division:", num1 // num2)
print("Exponentiation:", num1 ** num2)
print("")

print("Before swap:", num1, num2)
num1, num2 = num2, num1
print("After swap:", num1, num2)
print("")

radius = 7
area = math.pi * radius ** 2
print("Area of the circle with radius 7:", area)
print("")

square_root = math.sqrt(num1)
print("Square root of num1:", square_root)
