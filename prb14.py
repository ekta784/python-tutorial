# create tables folder and write from here tables of 1 to 5
def tablegenerate(n):
    table=""
    for i in range(1,11):
        table += f"{n}x{i}={n*i}\n"
    
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(1,6):
    tablegenerate(i)

