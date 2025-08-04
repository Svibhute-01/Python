a, b, c = map(int, input("Enter three integers separated by space: ").split())
smallest=a if (a<b and a<c) else (b if b<c else c)
print("Smallest  of three is:",smallest)