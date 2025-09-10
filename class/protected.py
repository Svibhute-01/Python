class Student:

  
    def __init__(self,name,roll_no):
        self._name=name
        self._roll=roll_no
        print("Constructor is Called...")
        print("Name:", self._name)
        print("Div:", self._roll)
    
    def __del__(self):
        print("Destructor is called...")


    
        

obj = Student("snehal",36)   
