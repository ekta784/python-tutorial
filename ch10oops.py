#  class example
class Employee:
    language = "py" #class sttribute
    salary = 120000 #class sttribute

    def __init__(self): #called dunder method as _xyz_ ->autometically called
        print("it a constructyoer that initialize the object")
  
    # method
    def getInfo(self): #self is must passing argument in a method 
        print(self.salary)
   
    # static method that don't need object or a self arhument
    @staticmethod
    def greet():
        print("good morning")

ekta = Employee() #object of name ekta
ekta.name = "Eka D Vora"  #instance/object attribute
print(ekta.language,ekta.salary,ekta.name)

#below both are true 
Employee.getInfo(ekta) 
ekta.getInfo()

ekta.greet()



# to pass multiple argumets in constructor
# def _init_(self,name,language,salary):
        # self.name=name
        # self.language=language
        # self.salary=salary

#  ekta =Employee("ekta","js",120000)

# print(ekta.name,ekta.language,ekta.salary)