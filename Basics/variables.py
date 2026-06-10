# #integer data type

# num1 = 200
# num2 = -300
# num3 = 0

# print(num1, num2, num3)
# # You can also use the type() function to check the data type of a variable
# print(type(num1), type(num2), type(num3))

# #float data type

# float1 = 3.14
# float2 = -0.001
# float3 = 0.0
# print(float1, float2, float3)
# print(type(float1), type(float2), type(float3))

# # complex data type

# complex1 = 2 + 3j
# complex2 = -1 - 4j
# complex3 = 0 + 0j
# print(complex1, complex2, complex3)
# print(type(complex1), type(complex2), type(complex3))

# Converting between data types

# num1 = 100
# num2 = float(num1)  # Convert integer to float
# print(type(num2), num2)

# float1 = 3.14
# num3 = int(float1)  # Convert float to integer (truncates the decimal part)
# print(type(num3), num3)

# num1 = 200
# num2 = 300
# result = num1 + num2
# print("The sum of", num1, "and", num2, "is:", result)

# num1 = 200
# num2 = 300
# result = num1 - num2
# print("The difference between", num1, "and", num2, "is:", result)

# num1 = 200
# num2 = 300
# result = num1 * num2
# print("The product of", num1, "and", num2, "is:", result)

# num1 = 200
# num2 = 300
# result = num1 / num2
# print("The quotient of", num1, "and", num2, "is:", result)

# num1 = 200
# num2 = 300
# fdiv = num1 // num2
# print("The floor division of", num1, "and", num2, "is:", fdiv)

# num1 = 300
# num2 = 200
# # mod = num1 % num2
# # print("The modulus of", num1, "and", num2, "is:", mod)

# print(2 ** 3)  # Exponentiation: 2 raised to the power of 3 is 8
# print(round(3.14159))  # Rounding: rounds 3.14159 to the nearest integer, which is 3
# print(max(10, 20, 5))  # Maximum: returns the largest of the given numbers, which is 20
# print(min(10, 20, 5))  # Minimum: returns the smallest of
# print(num1>num2)  # Comparison: checks if num1 is greater than num2, returns True or False
# print(num1<num2)  # Comparison: checks if num1 is less than num2, returns True or False
# print(num1==num2)  # Equality: checks if num1 is equal to num2, returns True or False
# print(num1!=num2)  # Inequality: checks if num1 is not equal to num2, returns True or False
# print(num1>=num2)  # Greater than or equal to: checks if num1 is greater than or equal to num2, returns True or False
# print(num1<=num2)  # Less than or equal to: checks if num1 is less than or equal to num2, returns True or False


# String data type

# str1 = "Hello, World!"
# str2 = 'Python is great.'
# str3 = """This is a multi-line string.
# It can span multiple lines."""
# print(str1)
# print(str2)
# print(str3)
# print(type(str1), type(str2), type(str3))

#Formatting strings

# sub = "Python"
# wish = "Welcome to %s programming!" % sub
# print(wish)

# name = "Sneha"
# age = 21
# info = "My name is %s and I am %d years old." % (name, age)
# print(info)

# name = "Manya"
# age = 21
# info = "My name is {} and I am {} years old.".format(name, age)
# print(info)

# name = "Isha"
# age = 21
# info = f"My name is {name} and I am {age} years old."
# print(info)

# str = "Hello, World!"
# print(str[0])  # Accessing the first character 'H'
# print(str[7] , str[-2])  # Accessing the eighth character 'W' and the thirteenth character '!'
# print(str[0:5])  # Slicing the string to get 'Hello'
# print(str[7:12])  # Slicing the string to get 'World!'
# print(str[::5])  # Slicing the string to get 'Hello'

# str = "Hello"
# print(len(str))  # Output: 5

# str = "Hello, World!"
# print(str.upper())  # Output: "HELLO, WORLD!"
# print(str.lower())  # Output: "hello, world!"
# print(str.capitalize())  # Output: "Hello, world!"

# str = "Hello, World!"
# # print(str.replace("World", "Python"))  # Output: "Hello, Python!"
# # print(str.split(", "))  # Output: ['Hello', 'World!']
# # print(str.strip("!"))  # Output: "Hello, World"
# print(str.find("World"))  # Output: 7 (the starting index of "World")
# print(str.title())
# print(str.count("o"))  # Output: 2 (the number of occurrences of "o" in the string)
# print(str.startswith("Hello"))  # Output: True (checks if the string starts with "Hello")
# print(str.endswith("!"))  # Output: True (checks if the string ends with "

# list1 = ['python', 'java', 'c++']
# print(" ".join(list1))  # Output: "python java c++" (joins the list elements into a single string with a space as a separator)

# str1 = "Hello, World!"
# print("python" in str1)  # Output: False (checks if "python" is a substring of str1)
# print("Java" in str1)  # Output: True (checks if "Java" is a substring of str1)

# print("python" == "python")  # Output: True (checks if the string "python" is equal to "python")
# print("python" == "Python")  # Output: False (checks if the string "python" is equal to "Python", which is case-sensitive)

# str1 = "Welcome"
# str2 = "to"
# str3 = "Python"
# # Concatenating strings using the + operator
# result = str1 + " " + str2 + " " + str3
# print(result)  # Output: "Welcome to Python"

# str1 = "Hello"
# print(str1 * 3)  # Output: "HelloHelloHello" (repeats the string "Hello" three times)
# print("Python" > "Java")  # Output: True (compares the two strings lexicographically, "Python" is greater than "Java")

#Boolean data type

# bool1 = True
# bool2 = False
# print(bool1, bool2)
# print(type(bool1), type(bool2))

# Comparison operators return boolean values
# num1 = 10
# num2 = 20
# print(num1 > num2)  # Output: False (10 is not greater than 20)
# print(num1 < num2)  # Output: True (10 is less than 20)
# print(num1 == num2)  # Output: False (10 is not equal to 20)
# print(num1 != num2)  # Output: True (10 is not equal to 20)
# print(num1 >= num2)  # Output: False (10 is not greater than or equal to 20)
# print(num1 <= num2)  # Output: True (10 is less than or equal

#True or False

# print(bool(1))  # Output: True (non-zero integers are considered True)
# print(bool(0))  # Output: False (zero is considered False)
# print(bool(-5))  # Output: True (non-zero integers are considered True)
# print(bool(""))  # Output: False (empty strings are considered False)
# print(bool("Hello"))  # Output: True (non-empty strings are considered True)
# print(bool([]))  # Output: False (empty lists are considered False)
# print(bool([1, 2, 3]))  # Output: True (non-empty lists are considered True)

# #False

# print(bool(0))  # Output: False (zero is considered False)
# print(bool(""))  # Output: False (empty strings are considered False)
# print(bool([]))  # Output: False (empty lists are considered False)
# print(bool(None))  # Output: False (None is considered False)
# print(bool(False))  # Output: False (the boolean value False is considered False)
# print(bool(0.0))  # Output: False (zero float is considered False)
# print(bool(()))  # Output: False (empty tuples are considered False)
# print(bool({}))  # Output: False (empty dictionaries are considered False)

#And

# print(True and True)  # Output: True (both operands are True)
# print(True and False)  # Output: False (one operand is False)
# print(False and True)  # Output: False (one operand is False)
# print(False and False)  # Output: False (both operands are False)

#Or

# print(True or True)  # Output: True (at least one operand is True)
# print(True or False)  # Output: True (at least one operand is True)
# print(False or True)  # Output: True (at least one operand is True)
# print(False or False)  # Output: False (both operands are False)

#Not

# print(not True)  # Output: False (negation of True is False)
# print(not False)  # Output: True (negation of False is True)

# print(True + True)  # Output: 2 (True is treated as 1, so 1 + 1 = 2)
# print(True * 5)  # Output: 5 (True is treated as 1, so 1 * 5 = 5)
# print(False + False)  # Output: 0 (False is treated as 0, so 0 + 0 = 0)
# print(1+True)  # Output: 2 (True is treated as 1, so 1 + 1 = 2)
# print(0+False)  # Output: 0 (False is treated as 0, so 0 + 0 = 0)
# print(1+1+True)  # Output: 3 (True is treated as 1, so 1 + 1 + 1 = 3)
# print(True/False)  # Output: ZeroDivisionError (division by zero is not allowed, as False is treated as 0)

# print(True == 1)  # Output: True (True is considered equal to 1)
# print(False == 0)  # Output: True (False is considered equal to 0
# print(True == 0)  # Output: False (True is not considered equal to 0)
# print(False == 1)  # Output: False (False is not considered equal to

# #all() (and) (&)
# # print(all([True, True, True]))  # Output: True (all elements are True)
# print(10 > 5 and 5 > 3)  # Output: False (10 is greater than 5, but 5 is not greater than 3)
# print(10 > 5 , 5 > 3 , 3 > 1)  # Output: True (10 is greater than 5, 5 is greater than 3, and 3 is greater than 1)

# any() (or) (|)

# # print(any([False, False, True]))  # Output: True (at least one element is True)
# print(any([10>90 , 50>6 ,10>100]))  # Output: True (10 is not greater than 90, but 50 is greater than 6, and 10 is not greater than 100)

# None data type

# x = None
# print(x)  # Output: None (the value of x is None)
# print(type(x))  # Output: <class 'NoneType'> (the data type of x is NoneType)

# roll_number = None
# if roll_number is None:
#     print("Roll number is not assigned yet.")

# #list data type

# list1 = [1, 2, 3, 4, 5]
# print(list1)  # Output: [1, 2, 3, 4, 5] (the list is printed as it is)
# print(type(list1))  # Output: <class 'list'> (the data type of list1 is list)
# print(list1[0])  # Output: 1 (accessing the first element of the list)
# print(list1[2])  # Output: 3 (accessing the third element of the list)
# print(list1[0:3])  # Output: [1, 2, 3] (slicing the list to get the first three elements)
# print(list1[-5:-2])  # Output: [1, 2, 3] (slicing the list using negative indices to get the first three elements)

# list1[0]=1000
# print(list1)  # Output: [1000, 2, 3, 4, 5] (the first element of the list is updated to 1000)

# e1,e2,e3,e4,e5 = list1
# print(e1,e2,e3,e4,e5)  # Output: 1000 2 3 4 5 (all the elements of the list are printed)
# print(type(e1), type(e2), type(e3), type(e4), type(e5))  # Output: <class 'int'> <class 'int'> <class 'int'> <class 'int'> <class 'int'> (the data type of all the elements is int)

# e1,*list2,e2 = list1
# print(list2)  # Output: [2, 3, 4] (the middle elements of the list are stored in list2)

# for i in list1:
#     print(i)  # Output: 1000 2 3 4 5 (each element of the list is printed on a new line)

# Tuple data type

# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1)  # Output: (1, 2, 3, 4, 5) (the tuple is printed as it is)
# print(type(tuple1))  # Output: <class 'tuple'> (the data type of tuple1 is tuple)
# print(tuple1[0])  # Output: 1 (accessing the first element of the tuple)
# print(tuple1[2])  # Output: 3 (accessing the third element of the tuple)
# print(tuple1[0:3])  # Output: (1, 2, 3) (slicing the tuple to get the first three elements)
# print(tuple1[-5:-2])  # Output: (1, 2, 3) (slicing the tuple using negative indices to get the first three elements)    

# t5 = (1,1,1,2,5,2,3,4,5,6,7,8,9)
# print(t5.count(1))  # Output: 3 (the number of occurrences of 1 in the tuple)
# print(t5.index(5))  # Output: 4 (the index of the first occurrence of 5 in the tuple)
# print(t5.index(7)) # Output: 10 (the index of the first occurrence of 7 in the tuple)

# t6= (1, 2, 3, 4, 5)
# for i in t6:
#     print(i, end=" ")  # Output: 1 2 3 4 5 (each element of the tuple is printed on a new line)

# t7 = (1, 2, 3, 4, 5)
# print(2 in t7)  # Output: True (checks if 2 is an element of the tuple)
# print(6 in t7)  # Output: False (checks if 6 is an element of the tuple)
# print(2 not in t7)  # Output: False (checks if 2 is not an element of the tuple)
# print(6 not in t7)  # Output: True (checks if 6 is not an element of the tuple)

# t8 = (1, 2, 3, 4, 5)
# print(len(t8))  # Output: 5 (the number of elements in the tuple)
# print(max(t8))  # Output: 5 (the maximum element in the tuple)
# print(min(t8))  # Output: 1 (the minimum element in the tuple)
# print(sum(t8))  # Output: 15 (the sum of all the elements in the tuple)

# t10 = (1, 2, 3, 4, 5)
# list1 = list(t10)  # Convert the tuple to a list
# list1[0] = 1000  # Update the first element of the list
# new_t10 = tuple(list1)  # Convert the list back to a tuple
# print(new_t10)  # Output: (1000, 2, 3, 4, 5) (the updated tuple is printed)

# Dictionary data type

# d1 ={
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# print(type(d1))  # Output: <class 'dict'> (the data type of d1 is dict)
# print(d1.keys())  # Output: dict_keys(['name', 'age', 'city']) (the keys of the dictionary)
# print(d1.values())  # Output: dict_values(['Alice', 30, 'New York']) (the values of the dictionary)
# print(d1["name"])  # Output: "Alice" (accessing the value associated with the key "name")
# print(d1["age"])  # Output: 30 (accessing the value associated with the key "age")
# print(d1["city"])  # Output: "New York" (accessing the value associated with the key "city")
# for key in d1:
#     print(key)  # Output: name age city (each key of the dictionary is printed on a new line)


# Set data type

# numbers = {1,1, 2, 3, 4, 5}
# print(type(numbers))  # Output: <class 'set'> (the data type of numbers)
# print(numbers)  # Output: {1, 2, 3, 4, 5} (the set is printed as it is)
