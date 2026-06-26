import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Input (Hours Studied)
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Output (Marks)
y = np.array([20, 40, 60,80,100])

# Create Model
model = LinearRegression()

# Train Model
model.fit(x, y)

# Predict Marks for 6 hours
marks = model.predict([[6]])

print("Predicted Marks:", marks[0])