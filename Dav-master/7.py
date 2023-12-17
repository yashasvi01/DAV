# a. Perform one hot encoding of the last two columns of categorical data using the get_dummies() function.

import pandas as pd

# Assuming you have a DataFrame named 'students_df'
data = {
    'Name': ['Mudit Chauhan', 'Seema Chopra', 'Rani Gupta', 'Aditya Narayan', 'Sanjeev Sahni', 'Prakash Kumar',
             'Ritu Agarwal', 'Akshay Goel', 'Meeta Kulkarni', 'Preeti Ahuja', 'Sunil Das Gupta', 'Sonali Sapre',
             'Rashmi Talwar', 'Ashish Dubey', 'Kiran Sharma', 'Sameer Bansal'],
    'Birth_Month': ['December', 'January', 'March', 'October', 'February', 'December', 'September', 'August',
                    'July', 'November', 'April', 'January', 'June', 'May', 'February', 'October'],
    'Gender': ['M', 'F', 'F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'M'],
    'Pass_Division': ['III', 'II', 'I', 'I', 'II', 'III', 'I', 'I', 'II', 'II', 'III', 'I', 'III', 'II', 'II', 'I']
}

students_df = pd.DataFrame(data)

# One hot encoding using get_dummies()
students_encoded = pd.get_dummies(students_df[['Gender', 'Pass_Division']])

# Concatenate the original DataFrame with the encoded DataFrame
students_df = pd.concat([students_df, students_encoded], axis=1)

# Drop the original categorical columns
students_df.drop(['Gender', 'Pass_Division'], axis=1, inplace=True)

print("DataFrame after one hot encoding:")
print(students_df)

# b. Sort this data frame on the “Birth Month” column (i.e. January to December). Hint: Convert Month to
# Categorical.

# Convert 'Birth_Month' to Categorical and set the custom order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
students_df['Birth_Month'] = pd.Categorical(students_df['Birth_Month'], categories=month_order, ordered=True)

# Sort the DataFrame based on 'Birth_Month'
students_df = students_df.sort_values(by='Birth_Month')

print("\nDataFrame after sorting by Birth Month:")
print(students_df)

