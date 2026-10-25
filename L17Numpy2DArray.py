import numpy as np

# Create 2D array
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

# Print array and inspect shape
print(np_2d)
print(np_2d.shape)  # Output: (2, 5) -> 2 rows, 5 columns

# Single-type rule example: adding a string turns all elements into strings
np_2d_string = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                         [65.4, 59.2, 63.6, 88.4, "68.7"]])

print(np_2d_string)  

