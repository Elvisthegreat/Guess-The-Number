import random 
# Ask the user for their name
def ask_user_for_name():
    """
    Initializing process while user inputing their name,
    then a thank you message to be return along 
    with the name inputed 
    """
    print('Initializing...! Starting game in process...')
    user_name = input('Please enter a Name: ')
    return f"Thank you, {user_name}! Welcome.\n"
    
return_name = ask_user_for_name()
print(return_name)

"""
A count down function from 10 t0 0 before the game begin
"""
def loading_game_():
    print("Loading Game...\n")

    loading_game = 10
    while loading_game > -1:
        print(f"{loading_game} seconds...\n ")
        loading_game -=1
    print('Loading Completed\n')
loading_game_()

"""
Main game board section
"""

def guessing_game_step_one():
    # Guessing from 0 to 5 with 2 chances trial
    print("I'm thinking of a number from 0 to 5, can you guess what number it is?\n ")
    
    """
    Assigned the number am thinking to a variable guessing_number,
    and also the chances of trial for the user
    """
    guessing_number = random.randint(0, 0)
    trial = 2

    while trial > 0:

        guessing_the_number = int(input('Can you try and guess the number?'))
        
        if guessing_the_number == guessing_number:
            print(f"Well done! Nice guessing")
            return
        else:
            #Decrement the chances of trial by 1
            trial-=1

            #Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trial to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number}.")
                

guess_step_one = guessing_game_step_one()
print(guess_step_one)


def guessing_game_step_two():

    print("Welcome to stage 2\n")
    print("I'm thinking of a number from 1 to 10 , can you guess what number it is?\n ")

    guessing_number2 = 2
    trial = 3

    while trial > 0:
        guessing_the_number_two = int(input('Can you try and guess?'))

        if guessing_the_number_two == guessing_number2:
            print("Well done! You guessed correctly")
            return
        else:
            trial-=1
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trial to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number2}.")

guess_step_two = guessing_game_step_two()
print(guess_step_two)
print("Moving on to stage 3\n")

def guessing_game_step_three():

    print("Welcome to stage 3\n")
    print("I'm thinking of a number from 10 to 20 , can you guess what number it is?\n ")

    guessing_number3 = 19
    trial = 4
    
    while trial > 0:
        guessing_the_number_three = int(input('Can you try and guess?'))

        if guessing_the_number_three == guessing_number3:
            print("Well done! You guessed correctly")
            return
        else:
            trial-=1
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trial to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number3}.")

guess_step_three = guessing_game_step_three()
print(guess_step_three)
