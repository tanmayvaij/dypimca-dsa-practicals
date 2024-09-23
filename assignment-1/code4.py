# Create a program to count value occurred in list and sort the list in ascending and descending order

num1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
count = num1.count(5)
print("Number 5 occurred in list is: ", count, " times")

num1.sort()
print("Ascending order:", num1)

num1.sort(reverse=True)
print("Descending order: ", num1)
