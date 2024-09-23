# Data Structures Practical Assignments

## Assignment 1: List Operations (19-09-2024)

### 1. Create a list with numeric values and print all values, and specific index

```python
ages = [1, 2, 3, 4]
print(ages)

print("Third index value is: ", ages[3])
```

**Output:**

```
[1, 2, 3, 4]
Third index value is:  4
```

### 2. Add a new element to the list and change the current element value and remove any element from the list

```python
ages = [1, 2, 3, 4]
print(ages)

ages.append(25)
print(ages)

ages[3] = 44
print(ages)

ages.remove(25)
print(ages)
```

**Output:**

```
[1, 2, 3, 4]
[1, 2, 3, 4, 25]
[1, 2, 3, 44, 25]
[1, 2, 3, 44]
```

### 3. Create a program to add a list inside another list and pop at least one element

```python
num1 = [1, 2, 3, 4]
num2 = [1, 2]
num2.extend(num1)

print("List 1 is ", num1)
print("List 2 is ", num2)

num2.pop(3)
print("after popping: ", num2)
```

**Output:**

```
List 1 is  [1, 2, 3, 4]
List 2 is  [1, 2, 1, 2, 3, 4]
after popping:  [1, 2, 1, 3, 4]
```

### 4. Create a program to count value occurred in list and sort the list in ascending and descending order

```python
num1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
count = num1.count(5)
print("Number 5 occurred in list is: ", count, " times")

num1.sort()
print("Ascending order:", num1)

num1.sort(reverse=True)
print("Descending order: ", num1)
```

**Output:**

```
Number 5 occurred in list is:  2  times
Ascending order: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
Descending order:  [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
```

### 5. Create a program for a list of strings and sort in ascending and descending order

```python
charlist = ["telegram", "uber", "amazon", "iphone"]
print(charlist)

charlist.sort()
print("Ascending: ", charlist)

charlist.sort(reverse=True)
print("Descending: ", charlist)
```

**Output:**

```
['telegram', 'uber', 'amazon', 'iphone']
Ascending:  ['amazon', 'iphone', 'telegram', 'uber']
Descending:  ['uber', 'telegram', 'iphone', 'amazon']
```

### 6. Create a list of heterogeneous types and slice it

```python
l1 = [1, 2, 3, 4, "a", "b", "c", True, False]

print(l1[::])
print(l1[1:6:2])
print(l1[3:5])
```

**Output:**

```
[1, 2, 3, 4, 'a', 'b', 'c', True, False]
[2, 4, 'a']
[4, 'a']
```

### 7. Create a list inside a list and slice a specific element

```python
l1 = [1, 2, 3, 4, ["hello", "world"], 5, 6]
print(l1[4][0])
```

**Output:**

```
hello
```

### 8. Create a list and traverse its elements through a for loop

```python
li = [1, 2, 23, 4, 54, 56, 7, 8, 9]

for num in li:
    print(num)
```

**Output:**

```
1
2
23
4
54
56
7
8
9
```

---

## Assignment 2: Array Operations (23-09-2024)

### 9. Create an array with numeric values and print all values with the help of a for loop

```python
from array import array

num_arr = array("i", [2, 3, 4, 5, 6, 7, 8])

for num in num_arr:
    print(num)
```

**Output:**

```
2
3
4
5
6
7
8
```

### 10. Add a new element to the array and change the current element value and remove any element from the array

```python
from array import array

arr = array("i", [2, 3, 4, 5, 6, 7, 8])
print(arr)

arr.append(9)
print(arr)

arr[0] = 10
print(arr)

arr.remove(7)
print(arr)
```

**Output:**

```
array('i', [2, 3, 4, 5, 6, 7, 8])
array('i', [2, 3, 4, 5, 6, 7, 8, 9])
array('i', [10, 3, 4, 5, 6, 7, 8, 9])
array('i', [10, 3, 4, 5, 6, 8, 9])
```

### 11. Use the append and remove function in the numeric array

```python
from array import array

arr = array("i", [2, 3, 4, 5, 6, 7, 8])
print(arr)

arr.append(9)
print(arr)

arr.remove(7)
print(arr)
```

**Output:**

```
array('i', [2, 3, 4, 5, 6, 7, 8])
array('i', [2, 3, 4, 5, 6, 7, 8, 9])
array('i', [2, 3, 4, 5, 6, 8, 9])
```

### 12. Create two arrays, one for the product name and another for the product price and print the elements of two arrays (string concatenation should be there)

```python
from numpy import array

product_name = array(["titan-watch", "rolex-watch", "sonata-watch", "fastrack-watch"])
product_price = array([2000, 3000, 4000, 5000])

for i in range(4):
    statement = product_name[i] + ": $" + str(product_price[i])
    print(statement)
```

**Output:**

```
titan-watch: $2000
rolex-watch: $3000
sonata-watch: $4000
fastrack-watch: $5000
```

### 13. Create a program to create an array of strings and display all elements in upper and lowercase (use numpy library)

```python
from numpy import array, char

watches = array(["titan", "rolex", "sonata", "fastrack"])

ucw = char.upper(watches)
print(ucw)

lcw = char.lower(ucw)
print(lcw)
```

**Output:**

```
['TITAN' 'ROLEX' 'SONATA' 'FASTRACK']
['titan' 'rolex' 'sonata' 'fastrack']
```

### 14. Create a 2D array of numeric values and print that array

```python
from numpy import array

arr2d = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2d)
```

**Output:**

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

### 15. Convert a multidimensional array into a 1D array

```python
from numpy import array, reshape

arr2d = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2d)

arr1d = reshape(arr2d, -1)

print(arr1d)
```

**Output:**

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[1 2 3 4 5 6 7 8 9]
```
