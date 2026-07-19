# =====================================================
# LISTS
# =====================================================

# Q1.Create a list of 5 fruits and print the list.

fruits=["orange","mango","banana","apply","Strawberry"]
print(fruits)

# Q2.Take a list of numbers.
# Print the first and last element.
num=[1,2,3,4,5]
print(num[0],num[-1])

# Q3.Create a list of numbers.
# Add a new number at the end using append() and print the list.
num=[1,2,3,4,5]
print(num)

num.append(6)
print(num)

# Q4. Create a list of 5 numbers.
# Print each element using a for loop.
num=[1,2,3,4,5]
for i in num:
    print(i)

# Q5.Take a list of numbers and calculate the sum of all elements.
num=[1,2,3,4,5]
total=0

for i in num:
    total+=i
print(total)
    
# ==============================================================
# TUPLE
# ==============================================================
# Q1.Create a tuple of 5 colors and print it.

color=("red","green","black","blue","pink")
print(color)

# Q2.Print the first and last element of a tuple.
num=(1,2,3,4,5)
print(num[0])
print(num[-1])

# Q3.Count how many times 5 appears in this tuple:

num=(1,2,3,5,4,3,6,5,6,4,2,5,6,7,8,5)
print(num.count(5))

# Q4.Find the index of "Python" in:
tup=("SQL","python","World","Excel")
print(tup.index("python"))

# Q5.Loop through a tuple and print all elements.
tuple=(1,2,3,4,5,6)

for i in tuple:
    print(i)


# ==============================================================
# DICTIONARIES
# ==============================================================


# Q1.Create a dictionary with keys:
# name
# age
# city
# Print the dictionary.

dict={"name":"Rahul","age":17,"city":"Delhi"}
print(dict)

# Q2.Print only the value of "name" from the dictionary.
dict={"name":"Rahul","age":17,"city":"Delhi"}
print(dict["name"])

# Q3.Add a new key "course" with value "Python" and print the dictionary.
dict={"name":"Rahul","age":17,"city":"Delhi"}
dict["course"]="python"
print(dict)

# Q4.Loop through a dictionary and print keys.
dict={"name":"Rahul","age":17,"city":"Delhi"}
for key in dict:
    print(key)

# Q5.Loop through a dictionary and print key-value pairs.
dict={"name":"Rahul","age":17,"city":"Delhi"}
for key ,value in dict.items():
    print(key,"",value)


# ========================================================
# SET
# ========================================================

# Q1.Create a set of 5 numbers and print it.
num={1,2,3,4,5}
print(num)

# Q2.Add a new element to the set using add().
num={1,2,3,4,5}
num.add(6)
print(num)

# Q3.Remove an element from the set using remove().
num={1,2,3,4,5}
num.remove(2)
print(num)

# Q4. Check whether 10 exists in the set.
# Print True or False.

num={1,2,3,4,5,6,7,8,9,10}
print(10 in num)

# Q5.Loop through a set and print all elements.

num={1,2,3,4,5,6,7,8}
for i in num:
    print(i)