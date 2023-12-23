import random

def user_validation(username):
    # Check if the user exists in the database or file
    users = {}
    if username in users:
        return True
    else: 
        return False

def sign_in():
    """
    Asking the user to know if he's already a user if y,
    he will be prompt to enter his details, but if n, he will have to sign up
    """
    user_validating = True
    while user_validating:
        
        user_validating_sign_in = input("Are you already a user? y/n ")
        if user_validating_sign_in.upper() == "Y":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            # Check if the user exists after his inputs
            if user_validation(username):
                if users[username] == password:
                    print("Welcome back!")
                else:
                    print("Incorrect input. Please try again.")
            else:
                print('This input does not exist. Please sign up.')
                sign_up()
        elif user_validating_sign_in.upper() == "N":
            sign_up()
        else:
            print("Invalid input. Please enter 'y' or 'n'.\n")
def sign_up():

    print("Please sign up")
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Store the username and password in a database or file with curly braces
    users = {}
    users[username] == password
    print("Sign up successful!")
    sign_in()

sign_in()
user_validation()

# Ask the user for their name
def ask_user_for_name():
    """
    Initializing process while user inputing their name,
    then a thank you message to be return along 
    with the name inputed 
    """
    print('Initializing...! Starting game in process...')
    user_name = input('Please enter your sign up Name: ')
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

        guessing_the_number = int(input('Can you try and guess the number?\n'))
        
        if guessing_the_number == guessing_number:
            print(f"Well done! Nice guessing")
            return
        else:
            #Decrement the chances of trial by 1
            trial-=1

            #Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number}.")
                
"""
Assigning the called function to a variable
"""
guess_step_one = guessing_game_step_one()
print(guess_step_one)


def guessing_game_step_two():

    print("Welcome to stage 2\n")
    print("I'm thinking of a number from 1 to 10 , can you guess what number it is?\n ")

    guessing_number2 = 2
    trial = 3
      
    while trial > 0:
        guessing_the_number_two = int(input('Can you try and guess?\n'))

        if guessing_the_number_two == guessing_number2:
            print("Well done! You guessed correctly")
            return
        else: 
            #Decrement the chances of trial by 1
            trial-=1
            #Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number2}.")
"""
Assigning the called function to a variable
"""
guess_step_two = guessing_game_step_two()
print(guess_step_two)

def guessing_game_step_three():

    print("Welcome to stage 3\n")
    print("I'm thinking of a number from 10 to 20 , can you guess what number it is?\n ")

    guessing_number3 = 19
    trial = 4
    
    while trial > 0:
        guessing_the_number_three = int(input('Can you try and guess?\n'))

        if guessing_the_number_three == guessing_number3:
            print("Well done! You guessed correctly")
            return
        else:
            #Decrement the chances of trial by 1
            trial-=1
            #Returning how many trials left to the user to try again
            if trial > 0:
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number3}.")
"""
Assigning the called function to a variable
"""
guess_step_three = guessing_game_step_three()
print(guess_step_three)

def guessing_game_step_four():
    print("Welcome to stage 4\n")
    print("I'm thinking of a number from 20 to 30 , can you guess what number it is?\n ")

    guessing_number4 = 21
    trial = 5

    while trial > 0:
        guessing_the_number_four = int(input("Can you try and guess?\n"))

        if guessing_the_number_four == guessing_number4:
            print('Well done! You guessed correctly')
            return
        else:
            #Decrement the chances of trial by 1
            trial-=1
            if trial > 0: 
                #Returning how many trials left to the user to try again 
                print(f"Sorry you got it wrong! You have {trial} more trials to guess the number right.\n")
            else:
                print(f"Sorry, you have run out of trials. The number I was thinking of was {guessing_number4}.")  
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

