numbers = [1, 2, 3, 4, 5]

print("Basic List:", numbers)

numbers.append(6)
numbers.insert(0, 0)
print("After Modifications:", numbers)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1
    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

test_list = [64, 34, 25, 12, 22, 11, 90]
print("\nOriginal list:", test_list)
print("Searching for 25:", linear_search(test_list, 25))
print("Sorted list:", bubble_sort(test_list.copy()))