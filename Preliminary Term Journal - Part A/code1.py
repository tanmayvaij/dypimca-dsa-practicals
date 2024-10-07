"""
Create Array and perform the following operations:
a) Update array b)slice array element c)extend array d)append 
array e)remove element
"""

import array as arr

myarr = arr.array("i", [ 1, 2, 3, 4, 5, 6, 7, 8 ])
print(myarr)

myarr[0] = 9
print(myarr)

myarr = myarr[:5]
print(myarr)

myarr.extend([ 10, 11, 12, 13 ])
print(myarr)

myarr.append(20)
print(myarr)

myarr.remove(10)
print(myarr)
