import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Create a DataFrame with 3 columns and 50 rows
data = {
    'Column1': np.random.randint(1, 100, size=50),
    'Column2': np.random.randint(1, 100, size=50),
    'Column3': np.random.randint(1, 100, size=50)
}

df = pd.DataFrame(data)

# Replace 10% of values with null values
null_indices = np.random.choice(df.size, int(0.1 * df.size), replace=False)
df[null_indices] = np.nan

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# a. Identify and count missing values
missing_values = df.isnull().sum()
print("\na. Missing Values:")
print(missing_values)

# b. Drop the column having more than 5 null values
df = df.dropna(thresh=len(df) - 5, axis=1)

# c. Identify the row label having the maximum sum and drop that row
max_sum_row_label = df.sum(axis=1).idxmax()
df = df.drop(max_sum_row_label)

# d. Sort the DataFrame based on the first column
df = df.sort_values(by='Column1')

# e. Remove all duplicates from the first column
df = df.drop_duplicates(subset='Column1')

# f. Find the correlation between the first and second column and covariance between the second and third column
correlation_col1_col2 = df['Column1'].corr(df['Column2'])
covariance_col2_col3 = df['Column2'].cov(df['Column3'])

print("\nf. Correlation between Column1 and Column2:", correlation_col1_col2)
print("   Covariance between Column2 and Column3:", covariance_col2_col3)
