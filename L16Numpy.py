import numpy as np

# Define the height and weight lists first
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# Convert to NumPy arrays
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate Body Mass Index (BMI)
bmi = np_weight / np_height ** 2

print(bmi)