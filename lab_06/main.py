a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")

print("Types:", type(a), type(b), type(c))

try:
    print("String to int:", type(int(c)))
    print("String to float:", type(float(c)))
except ValueError:
    print("Error: Cannot convert string to number.")

person = {
    "name": "Elmurat",
    "age": 20
}

print("Person's name:", person.get("name"))
print("Person's age:", person.get("age"))

x = {4, 7, 9}

x.add(3)
x.remove(7)

print("Is 7 in x?", 7 in x)
print("Is 3 in x?", 3 in x)