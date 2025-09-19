class Student:
    

    def get_info(self):
       self.name=input("Enter Name of Student:")
       self.roll_no=input("Roll No:")
       self.unique_id=input("Unique ID:")

class Exam(Student):
      def get_marks(self):
          self.sub1=int(input("Enter marks of subject 1:"))
          
          self.sub2=int(input("Enter marks of subject 2:"))

      def result(self):
          self.marks=(self.sub1+self.sub2)
     

      def show(self):
         print("----Result----")
         print("Name:",self.name)
         print("Roll No:",self.roll_no)
         print("Unique ID:",self.unique_id)
         print("Total Marks:",self.marks)

obj1=Exam()

obj1.get_info()
obj1.get_marks()
obj1.result()
obj1.show()
        