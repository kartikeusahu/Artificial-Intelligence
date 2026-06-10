from doctest import Example

import pandas as pd

# Example 1
# print("Pandas version:", pd.__version__)

# Example 2
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)
# print(df)

# Example 3

# nums = [1, 2, 3, 4, 5]
# res = pd.Series(nums)
# print(res)

# Example 4

# data = ["Alice", "Bob", "Charlie"]
# res = pd.Series(data, index=['a', 'b', 'c'])
# print(res)

# Example 5

df = pd.read_csv("employees.csv")
# print(df)
# print(df.head())  # Display the first 5 rows of the DataFrame
# print(df.head(3))  # Display the first 3 rows of the DataFrame

# print(df.tail())  # Display the last 5 rows of the DataFrame
# print(df.tail(2))  # Display the last 2 rows of the DataFrame

# print(df.shape)  # Display the number of rows and columns in the DataFrame
# print(df.columns)  # Display the column names of the DataFrame
# print(df.info())  # Display a summary of the DataFrame, including data types and non-null counts

# print(df["Class"].describe()) # Display summary statistics for the "Class" column

# print(df[["Name", "Class"]])  # Display only the "Name" and "Class" columns of the DataFrame

# print(df[df["Class"] == "A"])  # Display rows where the "Class" column is equal to "A"

# print(df[df["Age"] > 30])  # Display rows where the "Age" column is greater than 30
# print(df[df["Age"] > 30][["Name", "Class"]])  # Display the "Name" and "Class" columns for rows where the "Age" column is greater than 30

# print (df.groupby("Class")["Age"].mean())  # Display the average age for each class

print(df.sort_values("Age"))  # Display the DataFrame sorted by the "Age" column in ascending order
print(df.sort_values("Age", ascending=False))  # Display the DataFrame sorted by the
