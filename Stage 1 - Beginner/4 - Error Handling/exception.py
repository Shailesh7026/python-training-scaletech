# try:
#     n = int(input("Enter a number: "))
# except ValueError as e:
#     print("Invalid input! Please enter a valid integer." , e )
# except Exception as e:
#     print("An error occurred: ", e)
    
# # The finally block executes whether an error occurred or not
# # finally:
# #     print("Error Handling completed.")
    
# # The else block executes only when no error occurs in the try block
# else:
#     print("No errors !!!")
  

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
    # print(f"An error occurred: {e}")


# assertions 

# def div(a,b):
#     # assert b!=0, "B should not be zero"
#     if b==0:
#         raise ValueError("B should not be zero")
#     return a / b

# div(10, 0) 


## User defined exception 

# class InvalidAgeError(Exception):
#     def __init__(self,age,msg="Age must be between 18 and 100"):
#         self.age = age
#         self.msg = msg
#         super().__init__(self.msg)

#     def __str__(self):
#         return f"{self.msg} : Provided age = {self.age}"
    
    
# try:
#     raise InvalidAgeError(12)
# except InvalidAgeError as e:
#     print(f"Error : {e}")


