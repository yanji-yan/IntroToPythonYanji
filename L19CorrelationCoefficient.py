import numpy as np

# Sample dataset: np_city with [height, weight]
np_city = np.array([
    [1.75, 70],
    [1.80, 85],
    [1.65, 60],
    [1.90, 95]
])

# Calculate correlation matrix between column 0 (height) and column 1 (weight)
# Verify: checks if the returned 2x2 matrix shows the relationship strength between variables
correlation = np.corrcoef(np_city[:, 0], np_city[:, 1])
print("Correlation Matrix:\n", correlation)