import numpy as np

# Regular Python lists
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# Python lists fail when applying operations directly:
# weight / height ** 2
# TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

# NumPy arrays handle element-wise operations correctly:
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)
# Output: array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])