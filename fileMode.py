
with open("sample.txt", "r+") as f:
        print("\nReading existing content in 'r+' mode:")
        print(f.read())
        f.write("\nAdded a line using 'r+' mode.")

with open("write_read.txt", "w+") as f:
    f.write("This file is opened in 'w+' mode.\n")
    f.seek(0)  
    print("\nContent of write_read.txt in 'w+' mode:")
    print(f.read())