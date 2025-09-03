
with open("sample.txt","w") as file:
    file.write("Welcome to file handling\nThis is line 2\nThis is line 3")


file1 = open("sample.txt","r") 


content = file1.read()

print("File content:",content)


file1.seek(0)


line1 = file1.readline()
print("First line ->", line1)


file1.seek(0)



print(file1.readlines())

file1.close()
