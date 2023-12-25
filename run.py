# import the random module
import random

"""
Imported pickle to save complex data structure
to the dictionary
"""
import pickle

# imported time
import time
 
# Users dictionary storage
users = {}

def load_users():
    global users # Access the global variable users
    try:
        # Open the file in binary read mode
        with open("users.pickle", "rb") as f:
            # Load the dictionary from the file
            users = pickle.load(f)
    except FileNotFoundError:
        # If the file does not exist, create an empty dictionary
        users = {}

# Define a function to save the dictionary to a file
def save_users():
    global users # Access the global variable users
    # Open the file in binary write mode
    with open("users.pickle", "wb") as f:
        # Dump the dictionary to the file
        pickle.dump(users, f)

load_users() # Load the dictionary from the file


def user_validation(username):
    # Check if the user exists in the database or file
    # Global keyword to access dictionary storage
    global users
    if username in users:
        return True
    else: 
        return False

def sign_in():
    """
    Asking the user to know if he's already a user if Y,
    he will be prompt to enter his user's details, but if N, he will have to sign up
    """
    user_validating = True
    while user_validating:
        
        user_validating_sign_in = input("Do you already have an account? Y/N \n")
        if user_validating_sign_in.upper() == "Y":
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")
            # Check if the user exists after his inputs
            if user_validation(user_name):
                if users[user_name] == user_password:
                    print("Welcome back!\n")

                    # Break the looping if user is validated
                    user_validating = False

                else:
                    print("Incorrect input. Please try again.")
            else:
                print('This input does not exist.\n')

                # Call the sign_up function if the user input does not exist
                sign_up()

                # Break the looping after signing up
                user_validating = False

        elif user_validating_sign_in.upper() == "N":
            sign_up()

            #Break the looping after signing up
            user_validating = False

        else: 
            #Return invalid input if the user enter a different option
            print("Invalid input. Please enter 'y' or 'n'.\n")

def sign_up():

    print("Please sign up \n")
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Store the username and password in a dictionary
    users[username] = password
    print("Sign up successful!\n")

#Calling the main sign_in function in the program
sign_in()

# Ask the user for their name
def ask_user_for_name():
    """
    Initializing process while user inputing their name,
    then a thank you message to be return along 
    with the name inputed 
    """
    print('Initializing...! Starting game in process...')
    time.sleep(2)
    user_name = input('Please enter your sign up Name: ')
    return f"Thank you, {user_name}! Welcome to the guessing world.\n"
    
return_name = ask_user_for_name()
print(return_name)

# Research.  save users details
save_users()

"""
A count down function from 10 t0 0 before the game begin
"""
def loading_game_():
    print("Loading Game...\n")

    loading_game = 10
    while loading_game > -1:
        print(f"{loading_game} seconds...\n ")
        loading_game -=1
        time.sleep(1) # Pause every 1 seconds
    print('Loading Completed!\n')
loading_game_()

"""
Main game board section
"""

def guessing_game_step_one():
    # Guessing from 0 to 5 with 2 chances trial
    time.sleep(1)
    print("I'm thinking of a number from 0 to 5, can you guess what number it is?\n ")
    
    """
    Assigned the number am thinking to a variable guessing_number,
    and also the chances of trial for the user
    """
    guessing_number = random.randint(0, 5)
    trial = 2

    while trial > 0:

        # Use a try and except block to validate the user input
        try:
            guessing_the_number = int(input('Can you try and guess the number?\n'))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue
        
        if guessing_the_number == guessing_number:
            print(f"Well done! Nice guessing\n")
            return True
        
        else:
            # Decrement the chances o f trial by 1
            trial-=1

            #Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number}.")
                return False

"""
Assigning the called function to a variable
"""
guess_step_one = guessing_game_step_one()
print(guess_step_one)


def guessing_game_step_two():

    print("Welcome to stage 2\n")
    print("I'm thinking of a number from 1 to 10 , can you guess what number it is?\n ")

    guessing_number2 = random.randint(1, 10)
    trial = 3
      
    while trial > 0:

         # Use a try and except block to validate the user input
        try:
            guessing_the_number_two = int(input('Can you try and guess?\n'))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue

        if guessing_the_number_two == guessing_number2:
            print("Well done! You guessed correctly")
            return True
        else: 
            # Decrement the chances of trial by 1
            trial-=1
            # Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number2}.")
                return False
"""
Assigning the called function to a variable
"""
guess_step_two = guessing_game_step_two()
print(guess_step_two)

def guessing_game_step_three():

    print("Welcome to stage 3\n")
    print("I'm thinking of a number from 10 to 20 , can you guess what number it is?\n ")

    guessing_number3 = random.randint(10, 20)
    trial = 4
    
    while trial > 0:

         # Use a try and except block to validate the user input
        try:
            guessing_the_number_three = int(input('Can you try and guess?\n'))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue
         
        if guessing_the_number_three == guessing_number3:
            print("Well done! You guessed correctly")
            return True
        else:
            # Decrement the chances of trial by 1
            trial-=1
            # Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number3}.")
                return False
"""
Assigning the called function to a variable
"""
guess_step_three = guessing_game_step_three()
print(guess_step_three)

def guessing_game_step_four():
    print("Welcome to stage 4\n")
    print("I'm thinking of a number from 20 to 30 , can you guess what number it is?\n ")

    guessing_number4 = random.randint(20, 30)
    trial = 5

    while trial > 0:

         # Use a try and except block to validate the user input
        try:
            guessing_the_number_four = int(input("Can you try and guess?\n"))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue

        if guessing_the_number_four == guessing_number4:
            print('Well done! You guessed correctly')
            return True
        else:
            # Decrement the chances of trial by 1
            trial-=1
            if trial > 0: 
                # Returning how many trials left to the user to try again 
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number4}.")
                return False  
"""
Assigning the called function to a variable
"""
guess_step_four = guessing_game_step_four()
print(guess_step_four)


"""
This section of code's are not mine, found this from a research
carried out, and i thought it was also a good option to add to 
the game function
"""
def guess_the_number():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    for i in range(10):
        guess = int(input("Guess #" + str(i+1) + ": "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in " + str(i+1) + " guesses.")
            return
    print("Sorry, you didn't guess the number. It was " + str(number) + ".")

guess_the_number()
print("Congratulation for completing the game to the end")

