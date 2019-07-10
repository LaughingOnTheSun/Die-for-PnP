import random

def oneToSixRoll(x): #function for random die output, 6 different dice.
    if x == 1:
        print('You rolled a...')
        print(random.randint(1,4))
    if x == 2:
        print('You rolled a...')
        print(random.randint(1,6))
    if x == 3:
        print('You rolled a...')
        print(random.randint(1,8))
    if x == 4:
        print('You rolled a...')
        print(random.randint(1,10))
    if x == 5:
        print('You rolled a...')
        print(random.randint(1,12))
    if x == 6:
        print('You rolled a...')
        print(random.randint(1,20))    
    
def timeToRoll(): #function for choosing amount of die and which die to roll
    while True:
        print('Choose the amount of dice you want to roll with.')
        userDieCount = input()
        if userDieCount.isdigit() == True: #needs valid digit to continue
            print('You want to roll this many die: '+userDieCount)
            print('Choose which dice you want to roll\n1 = 4 sided die\n2 = 6 sided die\n3 = 8 sided die\n4 = 10 sided die \n5 = 12 sided die\n6 = 20 sided die')
            for i in range(int(userDieCount)): #looping through userDieCount until reaching zero to end loop.
                if i >= 0:
                    userDieChoice = int(input()) #user's input for the actual die to roll
                    if userDieChoice > 0 and userDieChoice <= 6:
                        userDieCount = int(userDieCount) - 1
                        oneToSixRoll(userDieChoice)#function taking Die Choice and outputting player's roll.
                        print('This is a valid die choice')
                        if userDieCount == 0:
                            print('ENDING ROLL\n\n\n')
                            break
                    else:
                        print('This is NOT a valid die choice')
        else:
            print('Not a valid number')
    
    
timeToRoll()
    
    
