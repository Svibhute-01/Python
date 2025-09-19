class Student:
    

    def get_info(self):
       self.name=input("Enter Name of Student:")
       self.roll_no=input("Roll No:")
       self.unique_id=input("Unique ID:")

class Exam(Student):
      def get_marks(self):
          self.sub1=int(input("Enter marks of subject 1:"))
          
          self.sub2=int(input("Enter marks of subject 2:"))
class Result(Exam):
      def result(self):
          self.marks=(self.sub1+self.sub2)

          self.percentage = self.marks / 2

         
          if self.percentage >= 90:
            self.grade = "A+"
          elif self.percentage >= 75:
            self.grade = "A"
          elif self.percentage >= 60:
            self.grade = "B"
          elif self.percentage >= 50:
            self.grade = "C"
          elif self.percentage >= 35:
            self.grade = "D"
          else:
            self.grade = "F (Fail)"
     

      def show(self):
         print("----Result----")
         print("Name:",self.name)
         print("Roll No:",self.roll_no)
         print("Unique ID:",self.unique_id)
         print("Total Marks:(out of 200)",self.marks)
         print("Percentage",self.percentage)
         print("Grade:",self.grade)

obj1=Result()

obj1.get_info()
obj1.get_marks()
obj1.result()
obj1.show()
        