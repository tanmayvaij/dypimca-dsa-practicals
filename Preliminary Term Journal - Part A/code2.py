"""
Create an empty list, take size of list from user and append one-one element in empty list.
"""

mylist = []
size = int(input("Enter list size:- "))
for i in range(size):
    mylist.append(int(input(f"Enter num {i+1}")))
print(mylist)
