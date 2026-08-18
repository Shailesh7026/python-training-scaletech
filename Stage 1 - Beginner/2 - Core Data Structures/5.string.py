str = "0123456789"

# indexing - slicing 
print(str[0])        # '0'
print(str[-1])       # '9'
print(str[1:3])      # '12'
print(str[1:])       # '123456789'
print(str[:4])       # '0123'
print(str[:])        # '0123456789'
print(str[::2])      # '02468'
print(str[1::2])     # '13579'
print(str[::-1])     # '9876543210'


# string is not mutable - cannot change the value of string
str = "Hello, World!"
# str[0] = "h"  # TypeError: 'str' object does not support item assignment


# string methods
str = "Hello, World!"
print("str.capitalize():", str.capitalize()) 
print("str.lower():", str.lower())
print("str.upper():", str.upper())
print("str.strip():", str.strip())
print("str.replace():", str.replace("World", "Universe"))
print("str.split():", str.split(","))
print("str.find():", str.find("World"))
print("str.index():", str.index("World")) # ⚠️ value error if not found
print("str.count():", str.count("l"))
print("str.partition():", str.partition("World"))


# string formatting
name = "Shailesh"
age = 20
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")


