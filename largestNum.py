n=int(input("How many numbers are there in lis?"))
print("Enter",n,"numbers:")
l=[]
for i in range (n):
  x=int(input())
  l.append(x)

largest=l[0]
for i in l:
  if(i>=largest):
    largest=i
  else:
    largest=largest
print("Largest Number is:" ,largest)