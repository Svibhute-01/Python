# Fibonacci series using while loop

n = int(input("Enter the number of terms: "))

# First two terms
t1 = 0
t2 = 1
count = 0

while count < n:
    print(t1, end=" ")
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    count += 1
