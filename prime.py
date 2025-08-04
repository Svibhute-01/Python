import math

n = int(input("Enter a number to check whether it is prime or not: "))

if n == 0 or n == 1:
    print("Number is not prime")
elif n == 2:
    print("Number is prime")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Number is prime")
    else:
        print("Number is not prime")
