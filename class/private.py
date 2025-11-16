class Student:

  
  
    

  
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    
    def __displayDetails(self):

      
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    def accessPrivateFunction(self):

      
        self.__displayDetails()


    
        

obj = Student("snehal",36,"CSE")   


print(obj._Student__name)
print(obj._Student__roll)
print(obj._Student__branch)
obj._Student__displayDetails()



obj.accessPrivateFunction()