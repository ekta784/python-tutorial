# # check number is prime or not
n=int(input("enter a number"))
for i in range(2,n):
    if (n%i==0):
        print("number is not prime")
        break
else:
    print("number is prime")

# fectorial

n=int(input("enter a number"))
i=0
for i in range(1,n+1):
    n=n*i
print(n)