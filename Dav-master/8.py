import pandas as pd

# Assuming you have a DataFrame named 'family_df'
data = {
    'Name': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome': [114000.00, 65000.00, 43150.00, 69500.00, 155000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]
}

family_df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income.
familywise_gross_income = family_df.groupby('Name')['MonthlyIncome'].sum()
print("a. Familywise Gross Monthly Income:")
print(familywise_gross_income)

# b. Calculate and display the member with the highest monthly income in a family.
member_highest_income = family_df.loc[family_df.groupby('Name')['MonthlyIncome'].idxmax()]
print("\nb. Member with the Highest Monthly Income in Each Family:")
print(member_highest_income)

# c. Calculate and display monthly income of all members with income greater than Rs. 60000.00.
income_greater_than_60000 = family_df[family_df['MonthlyIncome'] > 60000.00]
print("\nc. Monthly Income of Members with Income Greater than Rs. 60000.00:")
print(income_greater_than_60000)

# d. Calculate and display the average monthly income of the female members in the Shah family.
avg_income_shah_females = family_df[(family_df['Name'] == 'Shah') & (family_df['Gender'] == 'Female')]['MonthlyIncome'].mean()
print("\nd. Average Monthly Income of Female Members in the Shah Family:")
print(avg_income_shah_females)
