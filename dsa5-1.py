from array import *

def new_line():
    for i in range(1):
        print("\n")

array1 = array('i', [10, 20, 30, 40, 50])
array1.insert(1, 60)
for x in array1:
    print(x)

new_line()

array1.remove(40)
for x in array1:
    print(x)

# Linear Search
def linear_search(list, n, key):
    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1

list = [1, 3, 5, 6, 7]
n = len(list)
key = 7

result = linear_search(list, n, key)

if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found..")
    

binary_list = [12, 24, 32, 39, 45, 50, 54]
n = 45
# setting two pointer low & high
# Iterative Binary Search Function method Python Implementation
# It returns index of n in given list if present
# else return -1

def binary_search(list, n):
    low = 0
    high = len(list) - 1

    while low <= high:
        # Calculate the mid index
        mid = (high + low) // 2

        # 1st Comparison: Is list[mid] less than n
        if list[mid] < n:
            low = mid + 1 # Ignore the left half

        # 2nd Comparison: Is list[mid] greater than n
        elif list[mid] > n:
            high = mid - 1

        # 3rd Comparison: Is list[mid] equal to n
        else:
            return mid        
    return -1

res = binary_search(binary_list, n)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in binary_list")