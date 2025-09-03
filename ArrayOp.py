import array as arr


a = arr.array('i', [1, 2, 3])


print("Initial array:", *a)


a.append(4)
print("After append:", *a)


a.insert(2, 3)
print("After insert:", *a)


a.remove(1)   
print("After remove:", *a)


print("Popped element:", a.pop())
print("After pop:", *a)


print("Index of 3:", a.index(3))


a.reverse()
print("After reverse:", *a)


print("Occurrence of 2:", a.count(2))


a.extend([20, 12, 34])
print("After extend:", *a)


print("As list:", list(a))
