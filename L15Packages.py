# 1. Installing packages (run in terminal, not in Python script):
# pip install numpy

# 2. Importing an entire package
import numpy

array_1 = numpy.array([1, 2, 3, 4, 5])
print(array_1)

# 3. Importing a package with an alias (standard convention)
import numpy as np

array_2 = np.array([1, 2, 3, 4, 5])
print(array_2)

# 4. Importing a specific function from a package
from numpy import array

array_3 = array([1, 2, 3, 4, 5])
print(array_3)