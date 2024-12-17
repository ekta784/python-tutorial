class programmer:
    company = "Microsoft"
    
    def __init__(self,name,salary,pin):
        self.name= name
        self.salary= salary
        self.pin= pin

p= programmer("ekta",150000000,360000)
print(p.name,p.salary,p.pin,p.company)