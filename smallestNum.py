n=int(input("How many numbers are there in lis?"))
print("Enter",n,"numbers:")
l=[]
for i in range (n):
  x=int(input())
  l.append(x)

smallest=l[0]
for i in l:
  if(i<=smallest):
    smallest=i
  
    
print("Smallest Number is:" ,smallest)