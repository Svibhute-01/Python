n=int(input("Enter a number to calculate factorial "))
if(n==0):
    print("Factorial of 0 is:1")
else:
 fact=1
 for i in range(1,n+1):
    fact=fact*i
print("Factorial is:",fact)