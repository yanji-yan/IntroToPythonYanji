import numpy as np

# Define height_in (in inches)
height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)