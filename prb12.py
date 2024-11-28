def greter(a,b,c):
    if(a>b and a>c):
        return "a is greter"
    elif(b>a and b>c):
        return "b is greter"
    else:
        return "c is greter"

print(greter(2,925,5))

# sum of n using recursion
def sum(n):
    if(n==1): #necessory to prevent infinite loop - base condition
        return 1
    return sum(n-1)+n
a= int(input(" enter a number:"))
print(sum(a))


# pattern problem
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
pattern(5)