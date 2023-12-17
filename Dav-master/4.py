# please either dwonlaod or import excel files which are used here.

import pandas as pd

# Assuming you have two Excel files named 'day1.xlsx' and 'day2.xlsx'
# Load data into two dataframes


day1_df = pd.read_excel('First-excel path')
day2_df = pd.read_excel('Second-excel path')

# a. Perform merging of the two dataframes to find the names of students who attended the workshop on both days.
both_days_attendance = pd.merge(day1_df, day2_df, on='Name', how='inner')
print("\na. Names of students who attended the workshop on both days:")
print(both_days_attendance['Name'])

# b. Find names of all students who have attended the workshop on either of the days.
either_day_attendance = pd.merge(day1_df, day2_df, on='Name', how='outer')
print("\nb. Names of all students who attended the workshop on either of the days:")
print(either_day_attendance['Name'])

# c. Merge two dataframes row-wise and find the total number of records in the dataframe.
merged_row_wise = pd.concat([day1_df, day2_df], ignore_index=True)
print("\nc. Total number of records after merging row-wise:")
print(len(merged_row_wise))

# d. Merge two dataframes and use two columns names and duration as multi-row indexes. 
# Generate descriptive statistics for this multi-index.
merged_multi_index = pd.merge(day1_df, day2_df, on=['Name', 'duration'], how='inner')
print("\nd. Descriptive statistics for the merged data with multi-index:")
print(merged_multi_index.groupby(['Name', 'duration']).describe())
