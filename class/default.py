class Student:
    name = "Snehal Sachin Vibhute"
    div = "A"

   
    def __init__(self):
        print("Constructor is Called...")

    def show(self):
        print("Name:", self.name)
        print("Div:", self.div)


obj = Student()   
obj.show()
