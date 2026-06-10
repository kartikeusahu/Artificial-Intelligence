import numpy as np

# # 1D Array 

# a = np.array([10, 20, 30, 40, 50])

# # 2D Array

# b= np.array([[10, 20], [30, 40], [50, 60]])
# print(a.shape)  # Output: (5,)
# print(b.shape)  # Output: (3, 2)
# print(a.dtype)  # Output: int64 
# print(b.dtype)  # Output: int64
# print(a.ndim)   # Output: 1
# print(b.ndim)   # Output: 2

# # 3D Array

# c = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
# print(c.shape)  # Output: (2, 2, 2)
# print(c.dtype)  # Output: int64
# print(c.ndim)   # Output: 3

# # Example 2

# print(np.zeros((2, 3))) 
# print(np.ones((2, 3)))  
# print(np.full((2, 3), 7))  

# print(np.eye(3)) 
# print(np.arange(0, 10, 2)) 
# print(np.linspace(0, 1, 5))  

# Example 3

# a = np.array([1, 2, 3, 4, 5])
# print(a + 10) #output: [11 12 13 14 15]
# print(a * 2) #output: [ 2  4  6  8 10]
# print(a ** 2) #output: [ 1  4  9 16 25]
# b = np.array([10, 20, 30, 40, 50]) 
# print(a + b) #output: [11 22 33 44 55]
# print(a * b) #output: [10 40 90 160 250]
# print(a ** b) 
# print(a / b)

# Example 4

# a = np.array([10])
# b = np.array([20, 30, 40, 50])
# print(a + b)  # Output: [30 40 50 60]
# print(a * b)  # Output: [200 300 400 500]
# print(a / b)  # Output: [0.5 0.33333333 0.25 0.2]

# Example 5

# num = 10 
# arr1 = np.array([10,20,30,40])
# arr2 = np.array([[1,2],[3,4]])
# print(num + arr1)  # Output: [20 30 40 50]
# print(arr2+ num)  # Output: [[11 12]
#                    #          [13 14]]
# print(np.add(num, arr1))  # Output: [20 30 40 50]
# print(np.add(arr2, num))  # Output: [[11 12]
#                            #          [13 14]]
# print(np.multiply(num, arr1))  # Output: [100 200 300 400]
# print(np.multiply(arr2, num))  # Output: [[10 20]
#                                 #          [30 40]]
# print(np.subtract(arr1,arr2))  # Output: [[ 9 18]
#                                 #          [27 36]]
# print(np.divide(arr1,arr2))  # Output: [[10.          10.        ]
#                             #          [10.          10.        ]]
# print(np.power(arr1, 2))  # Output: [ 100  400  900 1600]
# print(np.power(arr2, 3))  # Output: [[ 1  8]
#                             #          [27 64]]
# print(np.mod(arr1, 3))  # Output: [1 2 0 1]
# print(np.remainder(arr1, 3))  # Output: [1 2 0 1]

# # Example 6
# arr = np.array([1, 2, 3, 4, 5])
# arr1 = np.reshape((5, 1))  # Reshape to a column vector
# print(arr1)  # Output: [[1]
#              #          [2]
#              #          [3]
#              #          [4]
#              #          [5]]
# arr2 = np.reshape((1, 5))  # Reshape to a row vector
# print(arr2)  # Output: [[1 2 3 4 5]]


# # Example 7  (Random Number Generation)

# print(np.random.rand(3))
# print(np.random.rand(2, 3))
# print(np.random.randint(0, 10, 5))

# Example 8: mean(), max(), min()

# marks = np.array([85, 90, 78, 92, 88])
# print(np.mean(marks))  # Output: 86.6
# print(np.max(marks))  # Output: 92
# print(np.min(marks))  # Output: 78

# Example 9

# arr1 = np.array([[1,2,3,4],
#                  [5,6,7,8]])
# print(np.sum(arr1))  # Output: 36
# print(np.sum(arr1, axis=0))  # Output: [ 6  8 10 12] rows are added together
# print(np.sum(arr1, axis=1))  # Output: [10 26] columns are added together

# Example 10: 

# arr = np.array([1, 2, 3, 4, 5])
# print(arr[0])  # Output: 1
# print(arr[1:4])  # Output: [2 3 4]
# print(arr[:3])  # Output: [1 2 3]
# print(arr[3:])  # Output: [4 5]
# print(arr[-1])  # Output: 5
# print(arr[-3:])  # Output: [3 4 5]

# Example 11:
# arr1 = np.array([1,2,3,4,5])
# print(np.sort(arr1)[::-1])  # Output: [5 4 3 2 1]