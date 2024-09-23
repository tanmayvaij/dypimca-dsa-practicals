# Create a program to add a list inside another list and pop at least one element

num1 = [1, 2, 3, 4]
num2 = [1, 2]

print("List 1 is ", num1)
print("List 2 is ", num2)

num1.append(num2)
print(num1)

num1[-1].pop(1)

print("after poping: ", num1)
