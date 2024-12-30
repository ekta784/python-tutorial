class TwodVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"vector is {self.i}i + {self.j}j")

class ThreedVector(TwodVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"vector is {self.i}i + {self.j}j + {self.k}k")

a= TwodVector(1,2)
a.show()
b=ThreedVector(1,5,7)
b.show()