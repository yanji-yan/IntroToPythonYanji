import numpy as np

# Define dummy background data so it runs on your computer
# (DataCamp provides these automatically, but local Python needs them explicitly defined)
baseball = [
    [74, 180, 22.99],  # [height in inches, weight in lbs, age]
    [74, 215, 34.69],
    [72, 210, 30.78]
]

updated = [
    [1, 2, 0.5],       # changes to add to each player's stats
    [0, -5, 0.5],
    [2, 3, 0.5]
]

# Create 2D numpy array: np_baseball
np_baseball = np.array(baseball)

# 1. Add np_baseball and updated (element-wise addition)
print("Updated Baseball Data:")
print(np_baseball + updated)

# 2. Create conversion factors: [inches to meters, lbs to kg, age unchanged]
conversion = np.array([0.0254, 0.453592, 1])

# 3. Multiply np_baseball with conversion (broadcasting converts units across each column)
print("\nConverted Units (Meters, Kg, Age):")
print(np_baseball * conversion)