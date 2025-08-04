a, b, c = map(int, input("Enter three integers separated by space: ").split())
largest=a if (a>b and a>c) else (b if b>c else c)
print("largest of three is:",largest)