# Add a new element to the array and change current element value and remove any element from the array

from array import array

arr = array("i", [2, 3, 4, 5, 6, 7, 8])
print(arr)

arr.append(9)
print(arr)

arr[0] = 10
print(arr)

arr.remove(7)
print(arr)
