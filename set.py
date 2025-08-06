s1={1,2,3,4,5,4,"snehal"}

s2={1,3,5,9}

print("Set 1:", s1)
print("Set 2:", s2)


s1.add(6)
print("After adding 6 to Set 1:", s1)

s1.update([7, 8])
print("After updating Set 1 with [7,8]:", s1)

s1.remove(2)
print("After removing 2:", s1)

s1.pop()
print("Ater pop",s1)


print("Union:", s1.union(s2))
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)
