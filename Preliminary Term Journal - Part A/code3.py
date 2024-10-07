"""
Create a list and perform following operations:
a)update b)count c)sort d)insert e)append f)extend g)pop
"""

mylist = [ 10, 3, 3, 5, 6, 7, 11, 8, 2, 1 ]
print(mylist)

mylist[0] = 9
print(mylist)

print(mylist.count(3))

mylist.sort()
print(mylist)

mylist.insert(3, 40)
print(mylist)

mylist.append(20)
print(mylist)

mylist.extend([ 10, 11, 12, 13 ])
print(mylist)

mylist.pop()
print(mylist)
