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
    return f"Thank you, {user_name} for your name!\n"
    
return_name = ask_user_for_name()
print(return_name)

def loading_game_():
    print("Loading Game...\n")

    loading_game = 10
    while loading_game > -1:
        print(f"{loading_game} seconds...\n ")
        loading_game -=1
    print('Loading Completed\n')
loading_game_()

"""
Main game board section, starting from 5 to 30 
"""
def guessing_game_step_one():
    # Guessing from 0 to 5 with 2 chances trial
    print("I'm thinking of a number from 0 to 5, can you guess what number it is?\n ")

    guessing_number = random.randint(0, 5)
    trial = 2

    while trial > 0:

        guessing_the_number = int(input('Can you try and guess?'))
        
        if guessing_the_number == guessing_number:
            print(f"Well done! Nice guessing")
            return
        else:
            trial-=1
            if trial > 0:
                print(f"No, You have {trial} more trial(s) to guess the number.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number}.")
                
guessing_game_step_one()