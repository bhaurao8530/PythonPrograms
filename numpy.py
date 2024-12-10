import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable
y = np.array([2, 4, 5, 4, 5])  # Dependent variable

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
X_new = np.array([6, 7, 8]).reshape(-1, 1)
y_pred = model.predict(X_new)

# Plot the data and the regression line
plt.scatter(X, y, label='Data Points')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(X_new, y_pred, color='green', label='Predictions')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# Print the coefficients and intercept of the model
print(f'Coefficient: {model.coef_[0]}')
print(f'Intercept: {model.intercept_}')
