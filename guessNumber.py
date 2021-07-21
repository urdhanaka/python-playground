# import random module to generate random number every code run
import random

if __name__ == "__main__":
    playing = True
    guesses = 0
    number = random.randint(1, 100)
    
while playing:
    userGuess = int(input("Guess the number: "))
    if userGuess == "exit":
        break
    guesses += 1
        
    if userGuess == number:
        playing = False
        print("your guess (" + str(userGuess) + ") is correct! You have guessed " + str(guesses) + " times!")
        break
    elif userGuess < number:
        if number % userGuess == 0:
            print("your guess is smaller and the number can be divisible by your number")
        else:
            print("your guess is smaller than the number")
    elif userGuess > number:
        if userGuess % number == 0:
            print("your number is greater than the number and can be divisible by the number")
        else:
            print("your number is greater than the number")