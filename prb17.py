class calc:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"square is {self.n*self.n}")
a=calc(4)
a.square()

class Demo:
    a=4
o=Demo()
print(o.a) #op=4 as a class attribute value
o.a=0
print(o.a) #op=0 as a instance attribute is now set