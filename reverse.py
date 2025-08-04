print("Palindrome")
n=int(input("Enter a number"))

reversed=0
while n > 0:
    digit = n % 10
    reversed=reversed*10+digit
    n = n // 10

print("reverse of number is:",reversed)