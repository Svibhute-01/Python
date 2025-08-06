l1 = [1, "snehal", 3.14, True, "Rose"]
l2 = list()

print("\nInitial List1:", l1)
print("Initial List2:", l2)


n = (input("\nEnter value to add into List1: "))
l1.append(n)
l1.append(1)  


n1 = (input("\nEnter value to add into List2: "))
l2.append(n1)


l1.insert(3, "Hello")
print("\nList1 after inserting 'Hello' at index 3:", l1)

l1.extend([6, 7])
print("List1 after extending with [6, 7]:", l1)


l1.remove(3.14)
print("List1 after removing 3.14:", l1)


l1.pop()
print("List1 after pop():", l1)


index_true = l1.index(True)
print("Index of True in List1:", index_true)


count_1 = l1.count(1)
print("Count of 1 in List1:", count_1)


print("Length of List1:", len(l1))


print("Is 'snehal' in List1?", "snehal" in l1)

# Copy
new_list = l1.copy()
print("Copy of List1:", new_list)
