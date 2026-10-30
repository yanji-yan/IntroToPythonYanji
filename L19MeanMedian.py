import numpy as np

# Sample dataset: np_city with [height, weight]
np_city = np.array([
    [1.75, 70],
    [1.80, 85],
    [1.65, 60],
    [1.90, 95]
])

# 1. Calculate the mean (average) of the first column (heights)
#    Verify: checks if mean returns a single numerical average value
mean_height = np.mean(np_city[:, 0])
print("Mean Height:", mean_height)

# 2. Calculate the median (middle value) of the first column (heights)
#    Verify: checks if median returns the middle point of sorted heights
median_height = np.median(np_city[:, 0])
print("Median Height:", median_height)