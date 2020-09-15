# Arrays / Dimensions
# Create 1-D Array

import numpy as np

Arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(type(Arr))

# Create 2-D Array

Arr2D = np.array([[1,2,3],[4,5,6]])

Arr3D = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

# Find dimension of the arrays
print(Arr.ndim)
print(Arr2D.ndim)
print(Arr3D.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

