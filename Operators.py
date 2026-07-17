# =====================================================================
# OPERATORS
# =====================================================================

# ARITHMETIC OPERATORS

# Q1.Take two integers as input and print:

# Addition
# Subtraction
# Multiplication
# Division 

a=int(input())
b=int(input())

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Q2.Take two integers as input and print the remainder using %.
a=int(input())
b=int(input())
c=a%b
print(c)

# Q3.Take two integers as input and print the quotient using //.
ab=int(input())
bc=int(input())
cc=(ab//bc)
print(cc)

# Q4.Take a number as input and print its square using **.
abc=int(input())
bbc=(abc**2)
print(bbc)

# Q5.Take three integers as input and calculate:
A=int(input())
B=int(input())
C=int(input())
print(A+B-C)

# COMPARISON OPERATORS

# Q1.Take two numbers as input and check whether they are equal.
ac=int(input())
ca=int(input())
print(ac==ca)
   
# Q2.Take two numbers as input and check whether the first number is greater than the second.
bc=int(input())
cb=int(input())
ad=bc>cb
print(ad)

# Q3.Take a person's age as input and check if the age is 18 or above.
person_age=int(input())
print(person_age >=18)

# Q4.Take a number as input and check whether it is less than 100.
number=int(input())
number2=number < 100
print(number2)

# Q5.Take two numbers as input and check whether they are not equal.
num1=int(input())
num2=int(input())
num3=num1 != num2
print(num3)

# LOGICAL OPERATORS

# Q1.Take age and citizenship (True/False) as input.
# Print True only if:
# age ≥ 18 and
# citizen is True

age = int(input("Enter age: "))
citizen = input("Are you a citizen? (True/False): ") == "True"
print(age >= 18 and citizen)

# Q2.Take two numbers as input.
# Check whether both are positive using and.

num=int(input())
num2=int(input())
print(num > 0 and num2 > 0)

# Q3.Take two numbers as input.
# Check whether at least one is positive using or.

numb=int(input())
numb2=int(input())
print(numb > 0 or numb2 > 0)

# Q4.Create a boolean variable:
# Print the opposite value using not.

is_logged_in=True
print(not is_logged_in)

# Q5.Take a username and password as input.
# Print True only if both are correct.

username=input("Enter the username:")
password=int(input("Enter the password:"))
print(username=="varun" and password == 12345)


# ASSIGNMENT OPERATORS

# Q1.Create a variable:
# Increase it by 5 using += and print the result.

num=10
num+=5
print(num)

# Q2.Create a variable:
# Decrease it by 8 using -= and print the result.
num=20
num-=8
print(num)

# Q3.Create a variable:
# Multiply it by 4 using *= and print the result.
num=10
num*=4
print(num)


# Q4.Create a variable:
# Divide it by 5 using /= and print the result.
num=25
num/=5
print(num)

# Q5.Create a variable:
# Square it using **= and print the result.
num=3
num**=2
print(num)


