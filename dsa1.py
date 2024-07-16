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