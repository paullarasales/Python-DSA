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
    