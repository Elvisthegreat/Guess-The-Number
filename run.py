import random 
# Ask the user for their name
def ask_user_for_name():

    print('Initializing...! Starting game in process...')
    user_name = input('Please enter a Name: ')
    return f"Thank you, {user_name} for your name!"
    
return_name = ask_user_for_name()
print(return_name)

def loading_game_():
    print("Loading Game.....")

    loading_game = 10
    while loading_game > 0:
        print(f"{loading_game} seconds... ")
        loading_game -=1
    print('Loading Completed')
loading_game_()