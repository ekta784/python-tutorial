# open another file and read or write it
f=open("file.txt")
data=f.read()
print(data)
f.close()

# now for write any file from here only
st="hii there...you are great,you are wonderful..!!"
f=open("myfile.txt","w")
f.write(st)
f.close() #it create a new file named myfile and write the content of st string

# f.readlines() for multiple line reading
# f.readline()  for single line read at once
# mode "a" append same string in last to program 

# with statement
with open("file.txt") as f:
    print(f.read()) 
# no need to explicitly close the file