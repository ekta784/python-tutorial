# # average of 3 numbers using function
# def avg():  #function defination
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=int(input("enter a number"))
#     average=(a+b+c)/3
#     print(average)

# avg() #function call

# function with argumets
def args(name,name2):
    print("hiii "+name)
    print(name2)
args("ekta","you are pretty!!") 

# return statement 
def args(name,name2):
    print("hiii "+name)
    print(name2)
    return args # whatever after return it prints in a exreturn hehehe gives hii ekta,you are pretty! ,hehehe
a=args("ekta","you are pretty!!") 
print(a)

# default args
def cat(name,color="red"):
    print("hii "+ name)
    print(color) #by default red or else what we gave is the output
cat("tom")
