import matplotlib.pyplot as plt

import pandas as pd



# Example 1 (Line Plot)

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple Line Plot")
# plt.show()

# Example 2 (Line Plot)

# x = [1, 2, 3, 4, 5]
# y1 = [10 , 20, 15, 25, 30]

# plt.title("Simple Line Plot")
# #plt.plot(x,y1 , color="blue", linestyle="--", marker="o") # linestyle = - , --, : marker = 0,x,*
# plt.plot(x,y1,'g*:')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# Example 2 (Bar Chart)

# categories = ["S", "N", "E", "H", "A"]
# values = [10, 15, 7, 12, 20]

# plt.bar(categories, values)
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Simple Bar Chart")
# plt.show()

 # Example 3 

# df = pd.read_csv("chart.csv")

# x = df["age"]
# y = df["salary"]

# plt.plot(x, y, 'b*--')
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.title("Age vs Salary")
# plt.show()

# Example 4 


x = ["Chanchal", "KitKat", "Manya", "Parvati", "Kartik"]
y1 = [85, 90, 78, 92, 88]

bars = plt.bar(
    x, y1,
    color=["red", "blue", "green", "orange", "purple"],
    width=0.5,
    edgecolor="pink",
    linewidth=2
)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        bar.get_height(),
        ha="center",
        va="bottom"
    )

plt.show()