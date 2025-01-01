try:
    a=int(input("enter a number:"))
    print(a)
except Exception as e:
    print(e)
print("thank you")

#zerodivision error
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if(b==0):
    raise ZeroDivisionError("programme is not ment to divide a number by zero")
else:
    print(f"the divisioj is {a/b}")


#try and else
try:
    a=int(input("enter a number:"))
    print(a)
except Exception as e:
    print(e)
else:
    print("i'm inside else loop")

#try and finally
def main():
    try:
        a=int(input("enter a number:"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("i'm inside else loop")
main()