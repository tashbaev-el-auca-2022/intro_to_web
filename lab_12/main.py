from math import acosh

class Car:
    def __init__(self, model, horsepower, color):
        self.model = model
        self.horsepower = horsepower
        self.color = color

    def display_info(self):
        return f"{self.color} {self.model} with {self.horsepower} horsepower."

    def increase_horsepower(self, increment):
        self.horsepower += increment
        return f"Horsepower increased to {self.horsepower} HP."

car = Car("Ford", 200, "Red")
print(car.display_info())
print(car.increase_horsepower(50))


class Dog:
    breed = "Labrador"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Alex", 3)
print(dog1.bark())

dog1.name = "Tagtugi"
print(dog1.bark())

dog2 = Dog("Ben", 5)

print(dog2.breed)
print(dog1.breed)

Dog.breed = "Golden Retriever"

print(dog2.breed)
print(dog1.breed)


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, password):
        return password == self.__password 

user = User("admin", "123")

print(user.login("123"))
print(user.login("123411"))


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited {amount}, new balance is {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrawn {amount}, new balance is {self.__balance}")
        else:
            print("Error: Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount("Connor", 1000)
account.deposit(500)
account.withdraw(100)

print(account.get_balance())


class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "sound"

class Dog(Animal):
    def make_sound(self):
        return "WOOF!"

class Cat(Animal):
    def make_sound(self):
        return "MEOW!"

dog = Dog("Jack")
cat = Cat("Jaque")
print(dog.make_sound())  # WOOF!
print(cat.make_sound())  # MEOW!


class Bird:
    def fly(self):
        return "Bird soars through the sky with natural force."
class Airplane:
    def fly(self):
        return "Airplane does the same as the birds but they are made of steel."
class Fish:
    def fly(self):
        return "Fish don't fly - they keep silence."
for entity in [Bird(), Airplane(), Fish()]:
    print(entity.fly())


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car_A(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

carA = Car_A()
bike = Bike()

carA.start_engine()
bike.start_engine()
