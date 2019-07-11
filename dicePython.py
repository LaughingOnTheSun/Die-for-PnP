import random
dieSum = 0 #global var for adding total after rolls.

def oneToSixRoll(x): #function for random die output, 6 different dice.
        global dieSum
        print('You rolled a...')
        a = random.randint(1,x)
        print(a)
        dieSum = dieSum + a
       
    
def timeToRoll(): #function for choosing amount of die and which die to roll
    while True:
        print('Choose the amount of dice you want to roll with.')
        userDieCount = input()
        if userDieCount.isdigit() == True: #needs valid digit to continue
            print('You want to roll this many die: '+userDieCount)
            print('What sided die do you want to roll (i.e 4, 6, 12, 20...etc)')
            for i in range(int(userDieCount)): #looping through userDieCount until reaching zero to end loop.
                if i >= 0:
                    userDieChoice = int(input()) #user's input for the actual die to roll
                    if userDieChoice > 0 and userDieChoice <= 20:
                        userDieCount = int(userDieCount) - 1
                        oneToSixRoll(userDieChoice)#function taking Die Choice and outputting player's roll.
                        if userDieCount == 0:
                            print('\n\nENDING ROLL')
                            print('The sum of your roll is: '+str(dieSum)+'\n')
                            break
                    else:
                        print('This is NOT a valid die choice')
        else:
            print('Not a valid number')
    
    
timeToRoll()
    
    
