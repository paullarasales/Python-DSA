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