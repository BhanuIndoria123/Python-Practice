# ===================================================
# PRINT FUNCTION
# ===================================================

# Q1.print your name
print("Bhanu Indoria")

# Q2. print name , age , country
name ="Rahul"
age=19
country="India"
print(name)
print(age)
print(country)

# Q3. print (Hye!..my name is Rahul ..i m 19 year old student i live in India..!!)
print(f"Hye! ..my name is {name}..i m {age}-year-old student and i live in {country}.")

# ====================================================
# INPUT FUNCTION
# ====================================================

#Q1.Take the user's name as input and print:
Name=input()
print("Hello",Name)

# Q2.Take two numbers as input and print their sum.
a=int(input())
b=int(input())
c=(a+b)
print(c)

#  Q3.Take your age as input and print:
Age=int(input())
print(f"I am  {Age}-year-old")

# Q4.Take your city name as input and print:
city=input()
print(f"Hye i live in {city}")

# Q5.Take first name and last name as input and print:
first_name=input()
last_name=input()
sername=first_name+last_name
print(sername)


# =========================================================
# INDENTATION FUNCTION
# =========================================================

# Q1.Write a program that prints "Positive Number" if the entered number is greater than 0.
num=int(input())
if num > 0:
    print("Postive number",num)
else:
    print("Negative Number",num)
print(num)


# Q2.Take the user's age. If age is 18 or above, print:
age=int(input())
if age >=18:
    print("You can vote")
else:
    print("you can't vote")


# Q3.Take a number as input. If it is even, print:
num=int(input())
if num % 2 ==0:
    print("Number is even")
else:
    print("Number is odd")


# Q4.Take marks as input. If marks are 40 or more, print:
mark=int(input())
if mark >=40:
    print("Pass")
else:
    print("Fail")


# Q5.Take a password as input. If the password is:
password=input()
if password =="python123":
    print("✅Correct Password")
else:
    print("❌Wrong Password")
