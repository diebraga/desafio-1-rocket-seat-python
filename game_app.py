# POO

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def salut(self):
#         return f"Hi my name is {self.name} I'm {self.age}"


# person = Person("Raul", 40)
# salut = person.salut()

# print(person.name)
# print(person.age)
# print(salut)

# Heranca
# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name

#     def walk(self):
#         return print(f"Animal {self.name} walks")

#     def make_sound(self):
#         pass


# class Cat(Animal):
#     def make_sound(self):
#         return "meow"

# class Dog(Animal):
#     def make_sound(self):
#         return "wolf"


# dog = Dog(name="Bento")
# cat = Cat(name="Gata")

# animals = [dog, cat]

# for animal in animals:
#     print(f"{animal.name} does {animal.make_sound()}")


# class BankAccount:
#     def __init__(self, funds) -> None:
#         self.__funds = funds

#     def cash_in(self, value):
#         if value > 0:
#             self.__funds += value

#     def cash_out(self, value):
#         if value > 0 and value <= self.__funds:
#             self.__funds -= value

#     def view_funds(self):
#         return self.__funds


# account = BankAccount(funds=1000)
# print(f"your funds {account.view_funds()}")
# account.cash_in(value=1000)
# print(f"your funds {account.view_funds()}")
# account.cash_out(value=500)
# print(f"your funds {account.view_funds()}")


# Abstraction

# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass


# class Car(Vehicle):
#     def __init__(self) -> None:
#         pass

#     def turn_on(self):
#         return "car turned on"

#     def turn_off(self):
#         return "car turned off"


# yellow_car = Car()
# print(yellow_car.turn_on())
# print(yellow_car.turn_off())
