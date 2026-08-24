class Phone:
    "This is basic doc for Phone class"
    
    def __init__(self,name,price):
        self.name = name
        self.__price = price
        
    def __str__(self):
        return f"{self.name} (Rs. {self.__price})"
    
    def __repr__(self):
        return f"Phone(name='{self.name}', price={self.__price})"
    
    def description(self):
        return f"Phone Name: {self.name} and Price: {self.__price}"
        

p1 = Phone("S21 Ultra",21000)
p2 = Phone("S22 Ultra",2000)
print(p1.description())

# Trying to edit obj directly
p1.__price = 100
p1._Phone__price = 0 # This gone edit the price 

print(p1.description())

print(p1.__dict__)
print(str(p1))
print(repr(p1))


print(Phone.__doc__)
print(p1.__doc__)


    