
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample student dataset
data = {
    "Name": ["Asha", "Ravi", "Priya", "Rahul", "Sneha",
             "Arjun", "Divya", "Kiran", "Meena", "Vijay"],
    "Marks": [85, 72, 90, 65, 88, 76, 95, 60, 82, 70],
    "Attendance": [95, 80, 98, 70, 92, 85, 99, 65, 90, 75],
    "StudyHours": [4, 2, 5, 1, 4, 3, 6, 1, 4, 2]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Save dataset as a CSV file
df.to_csv("student_performance.csv", index=False)

# Display the dataset
print("STUDENT DATASET")
print(df)

# Display basic information
print("\nDATASET INFORMATION")
print(df.info())

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS:", df.duplicated().sum())

# Find the highest and lowest marks
print("\nHighest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Marks:", df["Marks"].mean())

# Bar chart of student marks
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()

# Scatter plot: Study hours vs marks
plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("study_hours_vs_marks.png")
plt.show()
