f=open("prb13poem.txt")
content= f.read()
if("twinkle" in content):
    print("yes there is a twinkle")
else:
    print("No there is no a twinkle")

f.close()