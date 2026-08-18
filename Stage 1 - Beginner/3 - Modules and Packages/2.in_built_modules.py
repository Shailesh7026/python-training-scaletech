import math
import random
import datetime
import os


# math
print(math.sqrt(16)) # 4.0
print(math.factorial(5)) # 120
print(math.pi) # 3.141592653589793
print(math.floor(3.7)) # 3
print(math.ceil(3.7)) # 4

# random
print(random.randint(1, 10)) # random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry'])) # random choice from a list
print(random.shuffle([1, 2, 3, 4, 5])) # shuffles the list in place


# datetime
now  = datetime.datetime.now()
print(now) # current date and time
print(now.timetuple()) # time tuple

# formatted date
# %Y - year, %m - month, %d - day, %H - hour, %M - minute, %S - second
print(now.strftime("%Y-%m-%d %H:%M:%S")) 

print(now.today()) # current date and time


print(os.getcwd()) # current working directory
print(os.mkdir("test_dir")) # creates a new directory named "test_dir"
print(os.listdir()) # lists all files and directories in the current directory)