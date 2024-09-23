# Convert multidimensional array into 1D array

from numpy import array, reshape

arr2d = array([
    [ 1, 2, 3 ], 
    [4, 5, 6], 
    [7, 8, 9]
])

print(arr2d)

arr1d = reshape(arr2d, -1)

print(arr1d)
