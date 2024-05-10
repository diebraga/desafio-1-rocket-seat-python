class Character:
    def __init__(self, name: str, life: int, level: int) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_life(self):
        return self.__life

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"\n name: {self.get_name()}\n level: {self.get_level()}\n life: {self.get_life()}"


class Hero(Character):
    def __init__(self, name: str, life: int, level: int, skill: str) -> None:
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def show_details(self):
        return f"{super().show_details()}\n skill: {self.get_skill()}"


class Enemy(Character):
    def __init__(self, name: str, life: int, level: int, type: str) -> None:
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}\n skill: {self.get_type()}"


hero = Hero(name="Hero", life=100, level=5, skill="super punch")
enemy = Enemy(name="Bat monster", level=3, life=50, type="flyer")

print(f"Hero {hero.show_details()}")
print(f"Enemy {enemy.show_details()}")

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


# Heranca multipla

# class Animal():
#     def __init__(self, name) -> None:
#         self.name = name

#     def make_sound(self):
#         return f"{self.name} made a sound"


# class Mamal(Animal):
#     def breast_feed(self):
#         return f"{self.name} is breastfeedind"


# class Bird(Animal):
#     def fly(self):
#         return f"{self.name} is flying"


# class Bat(Mamal, Bird):
#     def make_sound(self):
#         return "bats make supersonic sounds"


# bat = Bat(name="batmonster")

# print(bat.name)
# print(bat.breast_feed())
# print(bat.fly())
# print(bat.breast_feed())

# def my_decorator(func):
#     def wrapper():
#         print("Antes da funcao ser chamada")
#         func()
#         print("depois da funcao")

#     return wrapper

#
