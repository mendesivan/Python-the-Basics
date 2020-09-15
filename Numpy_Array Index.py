# Indexing

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

print(arr[2] + arr[3])

# Access the 2nd element of 1st dim.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])
print('5th element on 2nd dim: ', arr[1, 4])

# Negative indexing

print('Last element from 2nd dim: ', arr[1, -1])