list_1 = [1, 2, 3, 'A', 'B', 7, 8, [10, 11]]
print(list_1)
x=list()
print(x)
tuple1 = (1, 2, 3, 4)
x = list(tuple1)
print(x)
del(x[1])
print("Deleted x 1", x)
# del(x)
x1 = [1, 2, 3, 4]
print(x1)
x1.append(5)
print("after append:", x1)
x2 = [6, 7, 8, 9]
x1.extend(x2)
print("Extend: ", x1)
# index pos 2, value = 12
x1.insert(2, 12)
print(x1)
x1.insert(1, [1, 2])
print(x1)
# pop method removes the specified index (or the last item if the index is not specified)
x1.pop()
print("Pop method: ", x1)
# pop specifying the index
x1.pop(4)
print("Pop specifying the index:", x1)
# Remove method removes the specified item from a given list.
x1.remove(12)
print("After using remove method: ", x1)
# Reverse the order of a given list
x1.reverse()
print("After reverse: ", x1)
# Sort method: sorts the element in ascending order
test = [1, 3, 5, 2, 4]
test.sort()
print(test)

# Slicing: slice out substrings, sub lists, sub tuples using index
# [Start:stop:steps]
    # Slicing will start from index and will go up to stop in step of steps.
    # Default value of start is 0.
    # Stop is last index of list
    # And for step default is 1

word='computer'
print(word[1:4])
print(word[1:6:2])
print(word[3:])
print(word[:5])
print(word[-1])
print(word[-3:])
print(word[:-2])
print(word[::-2])
print(word[::-1])