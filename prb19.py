class Animal:
    pass

class pet(Animal):
    pass

class Dog(pet):
    @staticmethod
    def bark():
        print("bhoww bhoww!!")

d=Dog()
d.bark()