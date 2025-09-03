import os
print("Get current working directory:",os.getcwd())

# os.mkdir("File Handling")
print("File Handling directory created")
print("List all files and folder within current directory",os.listdir())
# os.rename("File Handling","Directory Handling")
print("Renamed File Handling folder as Directory Handling")

print("Doess function.py exists?",os.path.exists(r"D:\TY\Python\function.py"))
print("Is it a file?", os.path.isfile(r"D:\TY\Python\function.py"))
print("Absolute path:", os.path.abspath(r"D:\TY\Python\function.py"))
os.chdir(r"D:\TY\Python\Directory Handling")
new_path = os.path.join("D:/TY/Python", "new_file.txt")
print("Joined path:", new_path)