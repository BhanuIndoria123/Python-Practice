# =======================================================
# FUNCTION DEFINATION
# =======================================================

# Q1.Find the maximum of two numbers.
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(3,4))


# Q2.Find the minimum of two numbers.
def minimum(a,b):
    if a > b:
        return b
    else:
        return a
print(minimum(3,4))

# Q3.Check if a number is prime
def is_prime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True

number=int(input("Enter a Number:"))
if is_prime(number):
    print("Prime")
else:
    print("Not Prime")


# Q4.Count vowels in a string.
def upper_vowel(text):
    count=0

    for char in text.upper():
        if char in "AEIOU":
                count+=1
    return count

sent=input("Enter a sentecnce:")
print(upper_vowel(sent))

# Q5.Reverse a string using a function.
def reverse(str):
    return str[::-1]
result=reverse("exam")
print(result)

# ======================================================
# ARGUMENTS & RETURNS
# ======================================================

# Q1.Create a function that takes 4 numbers and prints their average.        
def average(a,b,c,d):
    avg=(a+b+c+d)/4
    print(avg)

print(average(2,3,4,5))

# Q2.Create a function that takes a string and prints it in uppercase.
def uppercase(string):
    print(string.upper())
    
name=input("Enter a name:")
print(uppercase(name))

# Q3.Create a function that takes a list and prints the largest element.
def find_largest(number):
    largest=number[0]
    
    for num in number:                                          
        if num > largest:
            largest=num
    print("Largest elements:",largest)

my_list=[12,34,33,24,43]
find_largest(my_list)

# Q4.Create a function that takes a name and age and prints:
# My name is Rahul and I am 20 years old.
def intro(name,age):
    print(f"My name is {name} and I am {age} years old")

print(intro("Rahul",20))


# Q5.Create a function that takes a radius and prints the area of a circle.
import math
def find_area(radius):
    area=math.pi*radius**2
    print("Area Of Circle:",area)
print(find_area(4))

# =========================================================
# VARIABLE SCOPE
# =========================================================

# Q1.Create two different functions, each with a local variable named x. Print both values.
def first():
    x=10
    print("First Function x =",x)
def second():
    x=20
    print("Second Function x =",x)
(first)()
(second)()

# Q2.Try printing a local variable outside the function. What error do you get?
# def demo():
#     x=10
#     print(x)

# demo()
# print(x)

# Output
# 10
# NameError: name 'x' is not defined


# Q3.Create a global variable city = "Delhi" and print it inside two different functions.
city="Delhi"

def show_city():
    print(city)

def display_city():
    print(city)

show_city()
display_city()

# Q4.Create a function that modifies a global variable using global.
count=10
def change():
    global count
    count=20

change()

print(count)

# Q5.Predict the output of a program that has both a global and a local variable with the same name.
x=10

def demo():
    x=20 
    print("Inside function:",x)
demo()

print("Outside function",x)

# ==========================================================
# MODULES
# ==========================================================

# Q1.Generate a random password.
import random 
import string

def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=""

    for i in range(length):
        password+=random.choice(characters)
    return password
print("Random password:",generate_password(10))

# Q2.Generate a random OTP.
import random

def generate_otp():
    digits="0123456789"
    OTP=""

    for i in range(6):
        OTP+=random.choice(digits)
    return OTP
print("You OTP is:",generate_otp())

# Q3.Roll a dice (1–6).
import random

def roll_dice():
    dice="123456"
    dice_num=""

    for i in range(1,6):
        dice_num=random.choice(dice)
    return dice_num

print("You rolled is :",roll_dice())


# Q4.Print the current date and time.
from datetime import datetime

now=datetime.now()

print("Current Date and Time:",now)

# Q5.Calculate the area of a circle using math.pi.
import math

radius=float(input("Enter the radius:"))
area=math.pi*radius**2

print("Area of Circle:",area)