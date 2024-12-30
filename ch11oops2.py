# inheriance example
class Employee:
    company="ITC"
    def show(self):
        print(f"my name is {self.name}")

class Programmer(Employee):
    company="ITC Infotech"
    def show(self):
        print(f"my name is {self.name}")
    def showlanguage(self):
        print(f"my name is {self.name} and language i know is {self.language}")
a=Employee()
b=Programmer()
print(a.company,b.company)
print(b.show)