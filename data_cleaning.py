
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

print("Original Dataset:")
print(df.head())

# Step 2: Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Step 5: Remove duplicate rows
df = df.drop_duplicates()

# Step 6: Fill missing numerical values
numeric_cols = df.select_dtypes(include="number").columns

df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].mean()
)

# Step 7: Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Step 8: Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset saved!")

# Step 9: Create histograms
df[numeric_cols].hist(figsize=(10, 6), bins=15)
plt.suptitle("Student Performance Distribution")
plt.tight_layout()
plt.savefig("data_visualization.png")
plt.show()

# Step 10: Create correlation heatmap
if len(numeric_cols) > 1:
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm"
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()

print("\nProject completed successfully!")
