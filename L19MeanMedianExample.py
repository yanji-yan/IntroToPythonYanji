import numpy as np

# Sample dataset representing [height in inches, weight in lbs]
baseball = [
    [74, 180],
    [74, 215],
    [72, 210],
    [75, 205],
    [75, 190]
]
np_baseball = np.array(baseball)

# 1. Create np_height_in from the first column of np_baseball (index 0)
np_height_in = np_baseball[:, 0]

# 2. Print out the mean of np_height_in
print("Mean height:", np.mean(np_height_in))

# 3. Print out the median of np_height_in
print("Median height:", np.median(np_height_in))