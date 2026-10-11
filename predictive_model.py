
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Create a sample dataset
data = {
    "Reading": [65, 70, 80, 85, 90, 55, 60, 75, 88, 95],
    "Writing": [60, 72, 78, 82, 88, 58, 65, 73, 85, 93],
    "Math": [62, 71, 79, 84, 89, 56, 63, 74, 87, 94]
}

df = pd.DataFrame(data)

# Select features and target
X = df[["Reading", "Writing"]]
y = df["Math"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
print("Mean Absolute Error:",
      mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Plot results
plt.scatter(y_test, predictions)
plt.xlabel("Actual Math Scores")
plt.ylabel("Predicted Math Scores")
plt.title("Actual vs Predicted Math Scores")
plt.savefig("prediction_plot.png")
plt.show()

# Predict a new student's score
student = pd.DataFrame({
    "Reading": [80],
    "Writing": [75]
})

print("Predicted Math Score:",
      round(model.predict(student)[0], 2))
