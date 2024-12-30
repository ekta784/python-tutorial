# example of abstraction and encapsulation
class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e= emp()
e.a=45

e.name ="Ekta Vora"
print(e.fname,e.lname)
print(e.show())