import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Feature
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Label
Y = np.array([3, 5, 7, 9, 11, 13])

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.33, random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

print("Actual Salary:", Y_test)
print("Predicted Salary:", y_pred)

new_sal = model.predict([[7]])
print("New Salary:", new_sal[0])

print("Model Score:", model.score(X_test, Y_test))

plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")

plt.title("Linear Regression")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)

plt.show()