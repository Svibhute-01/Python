class MyContainer:
    def __init__(self):
        self.data = []  
    
   
    def __len__(self):
        return len(self.data)
    
   
    def __getitem__(self, index):
        return self.data[index]
    
    
    def __setitem__(self, index, value):
        
        if index < len(self.data):
            self.data[index] = value
        else:
           
            self.data.append(value)
    
    
    def __iter__(self):
        return iter(self.data)


# ---------- Testing ----------
c = MyContainer()
c[0] = "Python"
c[1] = "DSA"
c[2] = "Web Dev"

print("Length:", len(c))     
print("Item[1]:", c[1])     

c[1] = "Machine Learning"    
print("Updated Item[1]:", c[1])

print("Iterating:")
for item in c:               
    print(item)
