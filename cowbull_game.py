# import some modules to generate random number 
import random

def compare_number(number, guess):
    cowbull = [0, 0] # cowbull[0] is cow (the number and the position is correct), cowbull[1] is bull
    for i in range(len(number)):
        if guess[i] == number[i]:
            cowbull[0] += 1
        elif guess[i] in number:
            cowbull[1] += 1
    return cowbull

if __name__ == "__main__":
    playing = True
    number = str(random.randint(0, 9999))
    guesses = 0

while playing:
    guess = input("Guess the number: ")
    if guess == "exit":
        break
    cowbullcount = compare_number(number, guess)
    guesses += 1
    
    print("You have " + str(cowbullcount[0]) + " cows and " + str(cowbullcount[1]) + " bulls.")
    
    if cowbullcount[0] == 4:
        playing = False
        print("You win wtih " + str(guesses) + " guess! The number is "+ str(number))
        break
    else:
        print("Your guess is wrong")