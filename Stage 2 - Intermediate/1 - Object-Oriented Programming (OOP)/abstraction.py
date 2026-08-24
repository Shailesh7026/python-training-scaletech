from abc import ABC, abstractmethod

class Parent(ABC):
    
    @abstractmethod
    def method1():
        return
    
    # @abstractmethod  /// it can have body also 
    # def method1():
    #     print("with body")
    #     return
    
    def desc():
        print("Non abstract method")

class Child(Parent):
    
    def method1():
        pass
    
    def desc():
        print("child description")
        

obj = Child()
