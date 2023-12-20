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
    return f"Thank you, {user_name} for your name!"
    
return_name = ask_user_for_name()
print(return_name)

def loading_game_():
    print("Loading Game...\n")

    loading_game = 10
    while loading_game > -1:
        print(f"{loading_game} seconds...\n ")
        loading_game -=1
    print('Loading Completed')
loading_game_()

"""
Main game board section, starting from 5 to 30 
"""
def guessing_game_step_one():
    # Guessing from 1 to 5 with 2 chances trial
    print("I'm thinking of a number from 0 to 5, can you can what number it is? ")
    guessing_number = 0
    trial = 2