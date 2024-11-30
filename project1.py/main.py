# snake water gun game
# 1 for snake
# -1 for water
# 0 for water

import random
computer = random.choice([-1,1,0])
youstr=input("enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={ 1 : "snake",-1:"water",0:"gun"}
you = youDict[youstr]

print(f"you choose {reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer==you):
    print("it's a draw!!")

else:
    if(computer==-1 and you==1):
        print(" you win!!")

    elif(computer==-1 and you==0):
        print(" you lose!")

    elif(computer==1 and you==-1):
        print(" you lose!")

    elif(computer==1 and you==0):
        print(" you win!!")

    elif(computer==0 and you==-1):
        print(" you win!!")

    elif(computer==0 and you==1):
        print(" you lose!")

    else:
        print(" wrong input")

    # or just for understand do minuse of both value
    # if((computer - you)==-1 or (computer - you)==2):
    #     print("you lose!")
    # else:
    #     print("you win!!")

    # or a chatgpt code 
    # import random

# # Dictionary mapping choices to their names
# choices = {"s": "Snake", "w": "Water", "g": "Gun"}

# # Computer randomly selects a choice
# computer = random.choice(["s", "w", "g"])

# # User input
# you = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# # Check if input is valid
# if you not in choices:
#     print("Invalid input. Please enter 's', 'w', or 'g'.")
# else:
#     print(f"You chose: {choices[you]}")
#     print(f"Computer chose: {choices[computer]}")

#     # Determine the winner
#     if you == computer:
#         print("It's a draw!")
#     elif (you == "s" and computer == "w") or (you == "w" and computer == "g") or (you == "g" and computer == "s"):
#         print("You win!")
#     else:
#         print("You lose!")
