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