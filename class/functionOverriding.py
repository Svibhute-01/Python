class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getname(self):
        return self.name

    def getsalary(self):
        return self.salary


class Salary(Employee):
    def __init__(self, name, salary, inc):
        super().__init__(name, salary)
        self.inc = inc

    def getsalary(self):
        
        return self.salary + self.inc



s = Salary("Snehal", 30000, 3000)


print("Employee Name:", s.getname())

print("Salary Increment:", s.inc)
print("Total Salary:", s.getsalary())
