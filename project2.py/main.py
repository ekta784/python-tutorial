#a perfect guess with random numbers game
import random
n= random.randint(1,101)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a= int(input("enter a number to guess: "))
    if(a>n):
        print("enter a lower number")
    else:
        print("enter a higher number")

print(f"you have gussed a number  {n} correctly in {guesses} attempts")
