# Numeric 
a = 10 
b = 3.14
c = 2 + 3j

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>

# String
d = "Hello, World!"
print(type(d))  # <class 'str'>

# Boolean
e = True
print(type(e))  # <class 'bool'>

# Sequence
f = [1, 2, 3, 4, 5]  # List
g = (1, 2, 3, 4, 5)  # Tuple
h = {1, 2, 3, 4, 5}

print(type(f))  # <class 'list'>
print(type(g))  # <class 'tuple'>
print(type(h))  # <class 'set'>

# Dictionary
i = {"name": "Shailesh", "age": 20} # dict(name="Shailesh", age=20)
print(type(i))  # <class 'dict'>


#bytes
j = bytes([65, 66, 67]) 
print(j,type(j))  # ABC , <class 'bytes'>

# NoneType - used to represent the absence of a value or a null value
k = None
print(type(k))  # <class 'NoneType'>