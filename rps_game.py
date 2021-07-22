import random

choice = ["rock", "paper", "scissors"]
playing = True
choose = True
win = 0
draw = 0
lose = 0

def randomChoice():
    x = random.choice(choice)
    return x

while playing:
    x = randomChoice()
    while choose:
        userInput = input("Choose : ")
        if userInput in choice:
            choose = False
            continue
        else:
            print("your choice is invalid, choose again")
    
    if x == userInput:
        print("your choice is same as the computer (" + userInput + ")")
        draw += 1        
    elif x != userInput:
        if x == "paper":
            if userInput == "rock":
                print("you choose rock, the computer choose paper\nyou lose!")
                lose += 1
            elif userInput == "scissors":
                print("you choose scissors, the computer choose paper\nyou win!")
                win += 1
        elif x == "rock":
            if userInput == "scissors":
                print("you choose scissors, the computer choose rock\nyou lose!")
                lose += 1
            elif userInput == "paper":
                print("you choose paper, the computer choose rock\nyou win!")
                win += 1
        elif x == "scissors":
            if userInput == "paper":
                print("you choose paper,  the computer choose scissors\nyou lose!")
                lose += 1
            elif userInput == "rock":
                print("you choose rock, the computer choose scissors\nyou win!")
                win += 1
    
    askAgain = True            
    while askAgain:
        again = input("Do you want to play again? (y/n) ")
        if again == "y":
            choose = True
            askAgain = False
            continue
        elif again == "n":
            print("you have {} wins, {} loses and {} draw".format(str(win), str(lose), str(draw)))
            playing = False
            break
        else:
            print("your input is false, please use 'y' for yes or 'n' or no")
            again = input("Do you want to play again? (y/n)")