print("Palindrome")
n=int(input("Enter a number"))
temp=n
reversed=0
while n > 0:
    digit = n % 10
    reversed=reversed*10+digit
    n = n // 10

if(temp==reversed):
    print("It is palindrome")
else:
    print("it is not a palindrome") 