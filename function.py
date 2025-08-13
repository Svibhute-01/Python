def sum(n1):
    return 4+n1
print("Function to add values:")
print(sum(2))

def display(n1,n2=5):
    print("Value of n1 is:",n1)
    print("Value of n1 is:",n2)
    

print("Passing default value of n2")
display(4)
print("Overriding n2")
display(6,8)
print("\nLambda Function:")
add=lambda x:4+x
print(add(4))