a=input("enter name:")
print("good afternoon ", a)  #or using f string we can use variable in string
print(f"good afternoon {a}")

# detect double space
a="ekta D vora   a computer  engineer"
print(a.find("  ")) #return 11 which is index

# replace double space with sibgle space
a="ekta D vora  a computer  engineer"
print(a.replace("  "," "))  
