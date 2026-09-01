# function decorator
def fundecor(func):
    def inner(*args,**kwargs):
        print("Inside inner function")
        func(*args,**kwargs)
        print("Out Side inner function")
    return inner


def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun # class decorator
class Person:
    @fundecor # method decorator
    @staticmethod
    def greet(name):
        print(name)
        
print(Person.class_name)
Person.greet("Shailesh")





# Decorator Chaining

# def decor(fun):
#     def inner():
#         print("Inside inner function")
#         x = fun()
#         return x*x
#     return inner

# def decor1(fun):
#     def inner():
#         print("Inside inner2 function")
#         x = fun()
#         return x*2
#     return inner

# @decor1
# @decor
# def num():
#     return 10

# @decor
# @decor1
# def num1():
#     return 10

# print(num())
# print(num1())