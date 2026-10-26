import numpy as np

# Create 2D array: np_2d
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

# Select row 0 (heights): row 0, all columns
print(np_2d[0])

# Select a specific element: row 0, column 2 (1.71)
print(np_2d[0][2])
# Alternative notation (same result)
print(np_2d[0, 2])

# Select row 1 (weights), columns 1 through 3
print(np_2d[1, 1:4])

# Select column 2 across all rows (height and weight of 3rd person)
print(np_2d[:, 2])