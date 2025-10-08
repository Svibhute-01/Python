from abc import ABC, abstractmethod

class Teacher(ABC):  
    def __init__(self):
        self.marks = 50
    
    @abstractmethod
    def asg1(self):
        pass

    def asg2(self):
        pass


class Student(Teacher):
    completed = True

    def __init__(self, roll, m1, m2, m3):
        super().__init__()
        self.roll = roll
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.per = (self.m1 + self.m2 + self.m3) / 3

    def asg1(self):
        print("Assignment1 completed")

    def asg2(self):
        print("Assignment2 completed ")

    def display(self):
        self.per = (self.per + self.marks)/2
        print("Percentage", self.per)


std = Student(36, 56, 89, 76)
std.asg1()  
std.asg2()  
std.display() 
