
def read11Line(filename):
    
    with open(filename, "r") as f:
        f.seek(28)
        content=f.read()
    return content
      
       


