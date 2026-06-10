# def addition():
#     num1 = 5
#     num2 = 10
#     result = num1 + num2
#     # print("The result of addition is:", result)
#     print(f"The result of addition is: {result}")
# addition()


# def subtraction():
#     num1 = 15
#     num2 = 5
#     result = num1 - num2
#     return result

# x = subtraction()
# print(x)  # Output: 10

# y  = subtraction()
# print(y)  # Output: 10

# def multiplication(num1, num2):
#     result = num1 * num2
#     return result

# product = multiplication(4, 5)
# print(product)  # Output: 20

# def division(num1, num2):
#     if num2 != 0:
#         result = num1 / num2
#         return result
#     else:
#         return "Error: Division by zero is not allowed."
# quotient = division(10, 2)
# print(quotient)  # Output: 5.0

# def test_func():
#     print("This is a test function.")

# test_func()
# test_func()
# test_func()

# def test_func():
#     return [10, 20, 30]
# res = test_func()
# for num in res:
#     print(num)

# def test_func():
#     return [10, 20, 30]

# t1 = test_func()
# e1, e2, e3 = test_func()
# print(t1)  # Output: [10, 20, 30]
# print(e1, e2, e3)  # Output: 10 20 30

# def outer():
#     def inner():
#         return "Sneha"
#     return inner()
# print( outer())

# No Parameter - with return type

# def square():
#     num1 = 4
#     res = num1 *num1
#     return res

# result = square()
# print(result)  # Output: 16

# With Parameter - no return type
# def square(num1):
#     res = num1 * num1
#     print(res)

# square(5)  # Output: 25

# With Parameter - with return type
# def square(num1):
#     res = num1 * num1
#     return res
# result = square(6)
# print(result)  # Output: 36

# Keyword Arguments
# def student (name , age):
#     print(name , age)
# student(name = "Sneha" , age = 21)  # Output: Sneha 21
# student(age = 21  , name = "Kartikey")  # Output: Kartikey 21

# Default Arguments

# def student(name = "Manya"):
#     print(name)

# student()  # Output: Manya
# student("Sneha")  # Output: Sneha

# def test_ex(num1 , num2=20 , num3=30):
#     print(num1 , num2 , num3)

# test_ex(10)  # Output: 10 20 30
# test_ex(10 , 40)  # Output: 10 40 30
# test_ex(10 , 40 , 50)  # Output: 10 40 50

# Variable Length Arguments

# def add(*nums):
#     print(nums)
#     print(type(nums))
# add(1, 2, 3)  # Output: (1, 2, 3) <class 'tuple'>
# add(4, 5)  # Output: (4, 5) <class 'tuple'>

# def total(*prices):
#     print(sum(prices))

# total(10, 20, 30)  # Output: 60

# Keyword Variable Length Arguments

# def student(**details):
#     print(details)
#     print(type(details))

# student(name="Sneha", age=21)  # Output: {'name': 'Sneha', 'age': 21} <class 'dict'>
# student(name="Kartikey", age=22, city="Delhi")  # Output: {'name': 'Kartikey', 'age': 22, 'city': 'Delhi'} <class 'dict'>

# Global and Local Variables

# x = 10  # Global variable
# def test_func():
#     x = 5  # Local variable
#     print("Inside function:", x)  # Output: Inside function: 5

# test_func()
# print("Outside function:", x)  # Output: Outside function: 10

# Closures

# def outer_func(num):
#     def inner (num2):
#         return num + num2
#     return inner

# x = outer_func(10)
# result = x(5)
# print(result)  # Output: 15

# Lambda Functions
# res = lambda x: x * x
# print(res(4))  # Output: 16

# res = lambda num1, num2: num1 + num2
# print(res(10, 20))  # Output: 30

# students = [("Sneha", 21), ("Kartikey", 22), ("Manya", 20), ("Isha", 21) , ("Parvati", 22)]
# students.sort(key=lambda x: x[1])
# print(students)  # Output: [('Manya', 20), ('Sneha', 21), ('Isha', 21), ('Kartikey', 22), ('Parvati', 22)]

# Recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120

# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)
#     print(n)

# fun(3)  # Output: 3 2 1 1 2 3

# First Class Functions

# def hello():
#     print("Hello, World!")

# x= hello
# x()  # Output: Hello, World!

# map()
# nums = [1, 2, 3, 4, 5]
# res = list(map(lambda x: x * x, nums))
# print(res)  # Output: [1, 4, 9, 16, 25]

# filter()
# nums = [1, 2, 3, 4, 5]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)  # Output: [2, 4]

#defining a decorator function


# def decorator(func):
#     def wrapper():
#         print("Before the function call.")
#         func()
#         print("After the function call.")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# Generators

# def test_func():
#     yield 1 
#     yield 2
#     yield 3

# res = test_func()
# print(next(res))  # Output: 1
# print(next(res))  # Output: 2
# print(next(res))  # Output: 3


# LEGB Rule

# L - Local
# E - Enclosing
# G - Global
# B - Built-in

# x = "Global"
# def outer():
#     x = "Enclosing"
#     def inner():
#         x = "Local"
#         print(x)  # Output: Local
#     inner()
# outer()


