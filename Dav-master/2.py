import numpy as np

#a. Compute mean, standard deviation, and variance of a 2D random integer array along the second axis:
# Create a 2D random integer array
random_array = np.random.randint(1, 100, size=(3, 5))

# Compute mean, standard deviation, and variance along the second axis
mean_values = np.mean(random_array, axis=1)
std_dev_values = np.std(random_array, axis=1)
variance_values = np.var(random_array, axis=1)

print("Random Array:")
print(random_array)
print("\nMean along the second axis:", mean_values)
print("Standard Deviation along the second axis:", std_dev_values)
print("Variance along the second axis:", variance_values)

#b. Get the indices of the sorted elements of a given array:

import numpy as np

B = np.array([56, 48, 22, 41, 78, 91, 24, 46, 8, 33])

# Get the indices of the sorted elements
sorted_indices = np.argsort(B)

print("Original Array:", B)
print("Indices of sorted elements:", sorted_indices)

#c. Create a 2-dimensional array of size m x n and reshape it:
import numpy as np

# User inputs for m and n
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Create a 2D array of size m x n
array_mxn = np.random.randint(1, 100, size=(m, n))

print("\nOriginal Array:")
print(array_mxn)
print("Shape:", array_mxn.shape)
print("Type:", type(array_mxn))
print("Data Type:", array_mxn.dtype)

# Reshape the array into n x m
reshaped_array = array_mxn.reshape(n, m)

print("\nReshaped Array:")
print(reshaped_array)

#d. Test whether the elements are zero, non-zero, and NaN:
import numpy as np

# Create an array with zero, non-zero, and NaN elements
test_array = np.array([0, 5, 0, 8, np.nan, 12, 0])

# Test for zero, non-zero, and NaN elements
zero_indices = np.where(test_array == 0)[0]
nonzero_indices = np.where(test_array != 0)[0]
nan_indices = np.where(np.isnan(test_array))[0]

print("Original Array:", test_array)
print("Indices of Zero elements:", zero_indices)
print("Indices of Non-Zero elements:", nonzero_indices)
print("Indices of NaN elements:", nan_indices)


