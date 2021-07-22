import random

chooseNumber = True
roll = True
die = []
    
def get_diceValue():
    x = str(random.randint(1, 6))
    return x

while roll:
    i = 1
    while chooseNumber:
        diceTotal = input("how many dice(s) do you want to roll? (type exit if you want to exit) ")
        if diceTotal.isdigit():
            chooseNumber = False
        elif diceTotal == "exit":
            break
        else:
            print("Invalid input")
    
    if int(diceTotal) == i:
        die.append(get_diceValue())
    elif int(diceTotal) > i:    
        while int(diceTotal) + 1 > i:
            die.append(get_diceValue())
            i += 1
    print(*die, sep=", ")
    
    # reset the die list if the user want to roll again
    die.clear()
    
    # ask the user if they want to roll again
    askAgain = True
    again = input("Do you want to roll again? (y/n) ")
    while askAgain:
        if again == "y":
            askAgain = False
            chooseNumber = True
        elif again == "n":
            print("Thank you for rolling the dice")
            roll = False
            break
        else:
            print("your input is invalid, press y or n")
            again = input("Do you want to roll again? (y/n) ")
