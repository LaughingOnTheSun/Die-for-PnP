from random import randint

die_sum = 0 #global var for adding total after rolls.

# Changed x to sides, be sure to use meaningful variable names.
# Set a default in the function definition so you can call one_to_six_roll()
# and it will default to 6 sides.
def oneToSixRoll(sides=6): #function for random die output, 6 different dice.
        global die_sum
        result = random.randint(1, sides)
        print(f'You rolled a...{result}') # you can use f'some text {variable}' for format strings
        die_sum += result

# Changed timeToRoll to time_to_roll, in Python use snake case rather than camel case.
def time_to_roll(): #function for choosing amount of die and which die to roll.
    while True:
        # Rather than check a bunch if it is a digit and cast as int elsewhere, cast early.
        user_die_count = int(input(
            'Choose the amount of dice you want to roll with: '))

        print(f'You want to roll this many die: {user_die_count}')
        user_die_choice = int(input('What sided die do you want to roll (i.e 4, 6, 12, 20...etc)'))

        for dice in range(user_die_count):
            oneToSixRoll(user_die_choice)#function taking Die Choice and outputting player's roll.

        print('\n\nENDING ROLL')
        print(f'The sum of your roll is: {die_sum}\n')
        die_sum = 0

# Only call
if __name__ == '__main__':
    time_to_roll()
