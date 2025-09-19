class Student:
  

  
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print("Constructor is Called...")
        print("Name:", self.name)
        print("Div:", self.roll_no)
    
    def __del__(self):
        print("Destructor is called...")


    
        

obj = Student("snehal",36)   

print(Student.__dict__)
print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__bases__)