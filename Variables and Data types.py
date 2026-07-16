# ========================================================
 # VARIABLES AND DATA TYPES
# ========================================================

# Variable types:
# 1. Integer
# 2. Float
# 3. String
# 4. Booleans

# =========================================================
#  INTEGER TYPE QUESTIONS: 
# =========================================================

# Q1.Create an integer variable num = 50 and print its value.
num=50
print(num)

# Q2.Take two integers as input and print their multiplication.
a=5
b=4
c=(a*b)
print(c)

# Q3.Take a number as input and print its square.
abc=5
print(abc**2)

# Q4.Take your birth year as input and calculate your age.
birth_year=2004
present_year=2026
my_age=present_year-birth_year
print(my_age)

# Q5.Take three integers as input and print their average.
a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
avg=sum/3
print(avg)

# =========================================================
# FLOAT TYPE QUESTIONS:
# =========================================================

# Q1.Create a float variable for your height and print it.
height=5.5
print(height)

# Q2.Take two float numbers as input and print their addition.
ab=45.4
bc=53.2
print(ab+bc)

# Q3.Calculate the area of a circle.
import math

radius = float(input())
area = math.pi * radius * radius
print(area)

# Q4.Take price and discount percentage as input and calculate final price.
price=float(input())
discount=float(input())
discount_amount=(price*discount)/100

final_price=price-discount_amount
print(final_price)

# Q5.Convert Celsius temperature into Fahrenheit.
celsius = float(input())

fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# =========================================================
# STRING TYPE QUESTIONS:
# =========================================================

# Q1.Create a string variable with your name and print:
name="my name is Bhanu Indoria"
print(name)

# Q2.Take a name as input and print its length.
name=input()
print(len(name))

# Q3.Take first name and last name as input and join them.
first_name=input()
last_name=input()
sername=(first_name+" "+last_name)
print(sername)


# Q4.Convert a string into uppercase.
abc="rose"
print(abc.upper())

# Q5.Replace a word in a sentence.
sent="This is my pen"
sent=sent.replace("my","a")
print(sent)

# ==========================================================
# BOOLEAN TYPE QUESTIONS:
# ==========================================================

# Q1.Create a boolean variable:
abc=True
print(abc)

# Q2.Check if a number is greater than 10.
num =int(input())
print(num >10)
    
# Q3.Check whether a person can vote.
age=int(input())
print(age >=18)
    
# Q4.Check if two numbers are equal.
a=int(input())
b=int(input())
print(a==b)
    
# Q5.Create a login system.
password=input()
print(password=="python321")
