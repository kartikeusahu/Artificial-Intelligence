#Example-1

# class Test:
#     num1 = 200
#     num2 = 100

# obj = Test()
# x=obj.num1
# y=obj.num2
# addition = x + y
# print(addition)  # Output: 300

#Example-2
# (Instance variables)
# class Test:
#     # constructor
#     #used initilize members dynamically
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

# obj = Test(200, 100)
# x=obj.num1
# y=obj.num2
# addition = x + y
# print(addition)  # Output: 300

# Example-3

# class Test:
#     def _init_(self, name):
#         self.name = name

# obj = Test("Sneha")
# obj1 = Test("Isha")

# obj.name = "Manya"
# print(obj.name)  # Output: Manya    
# print(obj1.name)  # Output: Isha

# Example-4 (Instance Methods)

# class Test:
#     no parameter - no return type
#     def square (self):
#         num1 = 4
#         res = num1 *num1
#         print(res)
#     no parameter - with return type

#     def square (self):
#         num1 = 4
#         res = num1 *num1
#         return res
#     with parameter - no return type
#     def square (self , num1):
#         res = num1 *num1
#         print(res)
#     with parameter - with return type
#     def square (self , num1):
#         res = num1 *num1
#         return res

# obj = Test()
# obj.square()  # Output: 16
# result = obj.square()  # Output: 16
# print(result)  # Output: 16
# obj.square(5)  # Output: 25
# result = obj.square(6)  # Output: 36
# print(result)  # Output: 36

#Example-5 (Instance Methods and Instance Variables)

# class Test:
#     def __init__(self, num1):
#         self.num1 = num1

#     def square(self):
#         res = self.num1 * self.num1
#         return res
    
# obj = Test(4)
# result = obj.square()
# print(result)  # Output: 16 

# # Example-6 (Class Variables)

# class Test:
#     company = "Google"  # class variable

#     def __init__(self, name):
#         self.name = name

# obj = Test("Sneha")
# print(obj.company)  # Output: Google
# print(obj.name)  # Output: Sneha

# class Test:
#     name = "Kartikey"  # class variable

#     @classmethod
#     def my_func(cls, para1):
#         cls.name = para1

# Test.my_func("Sahu")
# print(Test.name)  # Output: Sahu

#Encapsulation

# class Bank:
#     def __init__(self):
#         self._balance = 10000
#     def show (self):
#         print(self._balance)

# b = Bank()
# b.show()  # Output: 10000

# Inheritance

# class Parent:
#     def m1 (self):
#         print("m1")

#     class Child(Parent):
#         pass

# c=Child()
# c.m1()

#Polymorphism

# class Parent:

#     def m1 (self):
#         print("m1")

# class Child(Parent):

#     def m1 (self):
#         print("m1 in child")

# c=Child()
# c.m1()  # Output: m1 in child

from abc import ABC, abstractmethod
class Test1(ABC):
    @abstractmethod
    def m1(self):
        pass    

class Test2(Test1):
    def m1(self):
        print("m1 in Test2")
t = Test2()
t.m1()  # Output: m1 in Test2