import random

# idk if this section is needed or not
if __name__ == "__main__":
    i = 1
    roll = True
    die = []
    
def get_diceValue():
    x = str(random.randint(1, 6))
    return x

while roll:
    diceTotal = int(input("how many dice(s) do you want? (type exit if you want to exit) "))
    if diceTotal == "exit":
        break
    
    if diceTotal == i:
        die.append(get_diceValue())
    elif diceTotal > i:    
        while diceTotal + 1 > i:
            die.append(get_diceValue())
            i += 1
    print(*die, sep=", ")
    
    # reset the die list and i in case the user want to roll again
    die.clear()
    i = 1
    
    # ask the user if they want to roll again
    askAgain = True
    again = input("Do you want to roll again? (y/n) ")
    while askAgain:
        if again == "y":
            askAgain = False
            continue
        elif again == "n":
            print("Thank you for rolling the dice")
            roll = False
            break
        else:
            print("your input is invalid, press y or n")
            again = input("Do you want to roll again? (y/n) ")
            