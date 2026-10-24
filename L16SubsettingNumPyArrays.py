import numpy as np

# Sample data 
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200] + [180] * 100
height_in = [74, 74, 72, 72, 73, 69, 69, 71] + [70] * 110

# Store weight and height as NumPy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])