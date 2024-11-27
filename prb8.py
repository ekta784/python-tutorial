#table of any number
n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")


# greet those whos name start with "s"
L = ["soham", "harry", "rahul", "sin"]

i = 0
while i < len(L):
    # Check if the name starts with 's'
    if L[i].startswith('s'):
        print(f"Hello, {L[i]}!")  # Greet the person
    i += 1  # Move to the next name
