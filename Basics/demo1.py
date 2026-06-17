#Tuples

#Tuples are immutable, ordered collections of items. They are defined using parentheses () and can contain elements of different data types.

#Creating a tuple

# t1=(1,2,3)
# print(t1)
# print(type(t1))


# t2 = ( 1,2,"null",4)
# print(t2)
# print(type(t2))

# t3 = (100,200,300,400,500)
# print(t3)
# print(type(t3))
# print(t3[0]) #Accessing elements of a tuple
# print(t3[1])
# print(t3[2])
# print(t3[:3])
# print(t3[2:])
# print(t3[-1])
# print(t3[-2])
# print(t3[-3:])


# t5 = (10,20,30,40,50)

# e1, e2, e3, e4, e5 = t5 #Unpacking a tuple
# e1, e2, *e3 = t5 #Unpacking with asterisk
# print(e1)
# print(e2)
# print(e3)
# print(e4)
# print(e5)

# t6=("ML","DL","NPL","GenAI")
# for elements in t6:
#     print(elements,end=" | ")

# t1 = (10,20,30)
# t2=(40,50,60)
# t3 = t1+ t2
# print(t3)
# print(t3*2)
# print(20 in t3)

# t1 = (100,200,300)
# i=0
# while i< len(t1):
#     print(t1[i])
#     i += 1

# t1 = (10,20,30,40,50,60)

# print(min(t1))
# print(max(t1))
# print(len(t1))
# print(sum(t1))

# students = (
#     (101,'Std1',20),
#     (102,'Std2',22),
#     (103,'Std3',24)

# )
# for sid, sname , age in students:
#     print(f"{sid} - {sname} - {age}")

# def calc(num1 , num2):
#     return num1+num2, num1-num2, num1*num2, num1/num2
# res = calc(200,100)
# add,sub,mul,div =  res
# print(add , sub , mul , div)