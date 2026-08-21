class Phone:
    def __init__(self,name,price):
        self.name = name
        self.__price = price
    
    def description(self):
        return f"Phone Name: {self.name} and Price: {self.__price}"
    
class SmartPhone(Phone):
    def __init__(self , name, price,camera_mp):
        self.camera_mp = camera_mp
        super().__init__(name,price)
        
    def description(self):
            return f"{super().description()} and Camera: {self.camera_mp}"
        
s1 = SmartPhone("S21 Ultra",10000,"100mp")

print(dir(s1))
print(s1.description())