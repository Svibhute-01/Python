   
def update(filename,content):
     with open(filename, "a") as f:
        f.write(content)
