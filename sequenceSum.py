import math


n = int(input("Enter a number (n): "))


sum_series = 0


for i in range(n + 1):
    sum_series += 1 / math.factorial(i)


print(f"Sum of the series up to 1/{n}! is: {sum_series}")
