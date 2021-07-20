# python project to check if the input number from user is odd or even number

def isOdd():
  userNumber = int(input("Insert your number: "))
  if userNumber % 2 == 0:
    print(str(userNumber) + "is a even number")
  else:
    print(str(userNumber) + "is a odd number")
    
isOdd()
