n=int(input("Enter value of n"))
t1=0
t2=1
for i in range(0,n):
  if(i==0):
    sum=0
  elif(i==1):
    sum=1
  else:
    sum=t1+t2
    t1=t2
    t2=sum
  print(sum,end=" ")
  
    