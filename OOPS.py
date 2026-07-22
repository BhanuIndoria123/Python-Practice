# ========================================================
# CLASS & OBJECT
# ========================================================

# Q1. Create a class Student and create one object.
class student:
    pass
student1=student()
print(student1)

# Q2. Create a class Car with two attributes (brand and color) and print them.
class car:
    brand="Toyota"
    color="Black"

car1=car()

print("Brand:",car1.brand)
print("Car:",car1.color)

# Q3. Create a class Person with a method greet().
class Person:
    def greet(self):
        print("Hello! Welcome.")
person1=Person()

person1.greet()

# Q4. Create two object of the same class:
class student:
    name="Rahul"
student1=student()
student2=student()

print(student1.name)
print(student2.name)

# Q5. Create a class Dog with attributes name and breed, then print them.
class dog:
    name="Tommy"
    breed="Labrador"

dog1=dog()
print("Dog Name:",dog1.name)
print("Breed:",dog1.breed)


# =================================================================
# CONSTRUCTOR (__INIT__)
# =================================================================

# Q1. create a student class using constuctor.
class student: 
    def __init__(self,name):
        self.name=name

student1=student("Bhanu")

print(student1.name)

# Q2. Create a Car class with brand and color.
class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    
car1=car("Toyota","Black")

print(car1.brand)
print(car1.color)

# Q3. Create an Employee class with name and salary.
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
employee1=employee("Rahul",50000)

print(employee1.name)
print(employee1.salary)

# Q4. Create two objects using different values.
class student:
    def __init__(self,name):
        self.name=name

student1=student("Bhanu")
student2=student("Rahul")

print(student1.name)
print(student2.name)

# Q5. Create a Book class with title and author.
class book:
    def __init__ (self,title,author):
        self.title=title
        self.author=author
        
book1=book("Python","Guido")

print(book1.title)
print(book1.author)

# ===================================================================
# INSTANCE VARIABLE & CLASS VARIABLE
# ===================================================================

# Q1. Create an instance variable name.
class student:
        def __init__(self,name):
            self.name=name

student1=student("Bhanu")
print(student1.name)

# Q2. Create a class variable school.
class student:
    school="Ducat"

student1=student()
student2=student()

print(student1.school)
print(student2.school)

# Q3. Create instance variables name and age.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=student("Rahul",20)
print(student1.name)
print(student1.name)

# Q4. Create a class variable country and print it using two objects.
class Person:

    country = "India"

person1 = Person()
person2 = Person()

print(person1.country)
print(person2.country)

# Q5. Create a class with both class and instance variables.        
class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

emp1 = Employee("Rahul")

print("Company:", emp1.company)
print("Employee:", emp1.name)

# ================================================================
# INSTANCE METHOD
# ================================================================

# Q1. Create an instance method to print a student's name.
class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)

student1=student("Bhanu")
student1.display()

# Q2. Create an instance method to print employee details.
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

emp=employee("Rahul",50000)
emp.details()

# Q3. Create a Car class and print brand and model.
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(self.brand)
        print(self.model)

car = Car("Toyota", "Fortuner")
car.show()

# Q4. Create a Book class and display title.
class Book:

    def __init__(self, title):
        self.title = title

    def display(self):
        print("Book:", self.title)

book = Book("Python")
book.display()

# Q5. Create a Dog class and print name and breed.
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def show(self):
        print(self.name)
        print(self.breed)

dog = Dog("Tommy", "Labrador")
dog.show()

# ==============================================================
# ENCAPSULATION
# ==============================================================

# Q1. Create a public variable.
class Student:

    def __init__(self):
        self.name = "Bhanu"

student = Student()
print(student.name)

# Q2. Create a protected variable.
class Student:

    def __init__(self):
        self._name = "Bhanu"

student = Student()
print(student._name)

# Q3. Create a private variable.
class Student:

    def __init__(self):
        self.__name = "Bhanu"

student = Student()

# print(student.__name)   # Error
# Output : AttributeError

# Q4. Access a private variable using a method.
class Student:

    def __init__(self):
        self.__name = "Bhanu"

    def show(self):
        print(self.__name)

student = Student()
student.show()

# Q5. Access a private variable using name mangling.
class Student:

    def __init__(self):
        self.__name = "Bhanu"

student = Student()
print(student._Student__name)

# =================================================================
# INHERITANCE
# =================================================================

# Q1. Single Inheritance
class animal:
    def sound(self):
        print("animal make a sound")
    
class dog(animal):
    def bark(self):
        print("Dog Barks")

dog1=dog()

dog1.sound()
dog1.bark()

# Q2. Single Inheritance (Student)
class Person:
    def display(self):
        print("I am a Person")
    
class student(Person):
    def study(self):
        print("I am Studing")

s=student()

s.display()
s.study()

# Q3. Multilevel Inheritance
class GrandFather:
    def house(self):
        print("Grandfather's house")

class Father(GrandFather):
    def car(self):
        print("Father's car")

class son(Father):
    def bike(self):
        print("Son's bike")
obj=son()

obj.house()
obj.car()
obj.bike()

# Q4. Multiple Inheritance
class Father:

    def money(self):
        print("Father's Money")


class Mother:

    def jewelry(self):
        print("Mother's Jewelry")


class Child(Father, Mother):

    def toy(self):
        print("Child's Toy")


obj = Child()

obj.money()
obj.jewelry()
obj.toy()

# Q5. Hierarchical Inheritance
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# ======================================================================
# POLYMORPHISM
# ======================================================================

# Q1. Create a parent class Animal with a method sound(). Override the method in the Dog class.
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()
dog.sound()

# Q2. Create a parent class Bird with a method fly(). Override the method in the Eagle class.
class Bird:

    def fly(self):
        print("Bird can fly")


class Eagle(Bird):

    def fly(self):
        print("Eagle flies very high")


obj = Eagle()

obj.fly()


# Q3. Create a parent class Shape with a method draw(). Override the method in the Circle class.
class Shape:

    def draw(self):
        print("Drawing Shape")


class Circle(Shape):

    def draw(self):
        print("Drawing Circle")


obj = Circle()

obj.draw()


# Q4. Create a parent class Person with a method intro(). Override the method in the Teacher class.
class Person:

    def intro(self):
        print("I am a Person")


class Teacher(Person):

    def intro(self):
        print("I am a Teacher")


teacher = Teacher()

teacher.intro()


# Q5. Create a parent class Animal with a method sound(). Override the method in the Cat class.
class Animal:

    def sound(self):
        print("Animal Sound")


class Cat(Animal):

    def sound(self):
        print("Cat Meows")


cat = Cat()

cat.sound()

# =============================================================================
# ABSTRACTION 
# =============================================================================

# Q1. Create an abstract class Vehicle with an abstract method start(). Implement it in the Car class.
from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("Car Started")
    
Car=car()
Car.start()


# Q2. Create an abstract class Animal with an abstract method sound(). Implement it in the Dog class.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()

dog.sound()

# Q3. Create an abstract class Shape with an abstract method area(). Implement it in the Square class.
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def area(self):
        print("Area of Square")


obj = Square()

obj.area()

# Q4. Create an abstract class Bank with an abstract method loan(). Implement it in the SBI class.
from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def loan(self):
        pass


class SBI(Bank):

    def loan(self):
        print("Home Loan")


bank = SBI()

bank.loan()

# Q5. Create an abstract class Employee with an abstract method salary(). Implement it in the Manager class.
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):

    def salary(self):
        print("Salary is 50000")


m = Manager()

m.salary()