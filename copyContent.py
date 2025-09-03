with open("sample.txt","r") as file1:
    content = file1.read()
    print(content)

with open("sample2.txt","a") as file4:
    file4.write(content)