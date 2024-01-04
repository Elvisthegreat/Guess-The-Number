import random  # import the random module

import pickle  # Imported pickle

import time  # imported time


def replay_game():
    """
    Restart the game function if user decided to play again
    """
    replay_game = True
    while replay_game:
        replay_again = input("Would you like to restart the game? Y/N: ")
        if replay_again.upper() == "Y":
            print('You have decided to restart again \n')
            """
            Call the functions to restart the game
            """
            guessing_game_step_one()
            guessing_game_step_two()
            guessing_game_step_three()
            guessing_game_step_four()
            guess_the_number()
        elif replay_again.upper() == "N":
            print("Now closing game...")
            replay_game = False
        else:
            print("Please enter Y/N: ")


users = {}  # Users dictionary storage


def load_users():
    """
    This section for loading user details always after they
    sign up, there details will be loaded each time the
    users input there register data
    """
    global users  # Access the global variable users
    try:
        # Open the file in binary read mode
        with open("users.pickle", "rb") as f:
            # Load the dictionary from the file
            users = pickle.load(f)
    except FileNotFoundError:
        # If the file does not exist, create an empty dictionary
        users = {}


def save_users():
    # Define a function to save the dictionary to a file
    global users  # Access the global variable users
    # Open the file in binary write mode
    with open("users.pickle", "wb") as f:
        # Dump the dictionary to the file
        pickle.dump(users, f)


load_users()  # Load the dictionary from the file


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
    he will be prompt to enter his user's details,
    but if N, he will have to sign up
    """
    user_validating = True
    while user_validating:

        user_validating_sign_in = input("Do you have an account? Y/N: ")
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

            # Break the looping after signing up
            user_validating = False

        else:
            # Return invalid input if the user enter a different option
            print("Invalid input. Please enter 'y' or 'n'.\n")


def sign_up():

    print("Please sign up \n")
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Store the username and password in a dictionary
    users[username] = password
    print("Sign up successful!\n")


sign_in()  # Calling the main sign_in function


# Ask the user for their name
def ask_user_for_name():
    """
    Initializing process while user inputing their name,
    then a thank you message to be return along
    with the name inputed
    """
    print('Initializing...! Starting game in process...')
    time.sleep(2)
    user_name = input('Please enter again your signed up Name: ')
    return f"Thank you, {user_name}! Welcome to the guessing world.\n"


return_name = ask_user_for_name()
print(return_name)

save_users()


def loading_game_():
    """
    A count down function from 10 t0 0 before the game begin
    """
    print("Loading Game...\n")

    loading_game = 10
    while loading_game > -1:
        print(f"{loading_game} seconds...\n ")
        loading_game -= 1
        time.sleep(1)  # Pause every 1 seconds
    print('Loading Completed!\n')


loading_game_()


def guessing_game_step_one():
    # first guessing section
    # Guessing from 0 to 5 with 2 chances trial
    time.sleep(1)
    print("I'm thinking of a number from 0 to 5.\n ")
    """
    Assigned the number am thinking to a variable guessing_number,
    and also the chances of trial for the user
    """
    guessing_number = random.randint(0, 5)
    trial = 2

    while trial > 0:

        # Use a try and except block to validate the user input
        try:
            guessing_the_number = int(input('Can you try and guess?: '))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue
        if guessing_the_number == guessing_number:
            print(f"Well done! Nice guessing")
            return True
        else:
            # Decrement the chances o f trial by 1
            trial -= 1

            # Returning how many trials left to the user to try again
            if trial > 0:
                print(
                    f"Sorry you got it wrong! You have {trial} more trial.\n"
                    )
            else:
                print(
                    f"Sorry, you have run out of trials.\n The number "
                    f"I was thinking of was {guessing_number}."
                      )
                return False


guess_step_one = guessing_game_step_one()
print(guess_step_one)


def guessing_game_step_two():
    # second guessing section
    print("Welcome to stage 2\n")
    print("I'm thinking of a number from 1 to 10.\n ")

    guessing_number2 = random.randint(1, 10)
    trial = 3
    while trial > 0:
        # Use a try and except block to validate the user input
        try:
            guessing_the_number_two = int(input('Can you try and guess?: '))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue

        if guessing_the_number_two == guessing_number2:
            print("Well done! You guessed correctly")
            return True
        else:
            # Decrement the chances of trial by 1
            trial -= 1
            # Returning how many trials left to the user to try again
            if trial > 0:
                print(
                    f"Sorry you got it wrong! You have {trial} more trials.\n"
                    )
            else:
                print(
                    f"Sorry, you have run out of trials.\n The number "
                    f"I was thinking of was {guessing_number2}."
                    )
                return False


guess_step_two = guessing_game_step_two()
print(guess_step_two)


def guessing_game_step_three():
    # Third guessing section
    print("Welcome to stage 3\n")
    print("I'm thinking of a number from 10 to 20.\n ")

    guessing_number3 = random.randint(10, 20)
    trial = 4
    while trial > 0:
        # Use a try and except block to validate the user input
        try:
            guessing_the_number_three = int(input('Can you try and guess?: '))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue

        if guessing_the_number_three == guessing_number3:
            print("Well done! You guessed correctly")
            return True
        else:
            # Decrement the chances of trial by 1
            trial -= 1
            # Returning how many trials left to the user to try again
            if trial > 0:
                print(
                    f"Sorry you got it wrong! You have {trial} more trials\n"
                    )
            else:
                print(
                    f"Sorry, you have run out of trials.\n The number "
                    f"I was thinking of was {guessing_number3}."
                    )
                return False


guess_step_three = guessing_game_step_three()
print(guess_step_three)


def guessing_game_step_four():
    # Fourth guessing section
    print("Welcome to stage 4\n")
    print("I'm thinking of a number from 20 to 30.\n ")

    guessing_number4 = random.randint(20, 30)
    trial = 5

    while trial > 0:
        # Use a try and except block to validate the user input
        try:
            guessing_the_number_four = int(input("Can you try and guess?: "))
        except ValueError:
            print('Invalid input. Please try again.\n')
            continue

        if guessing_the_number_four == guessing_number4:
            print('Well done! You guessed correctly \n')
            return True
        else:
            # Decrement the chances of trial by 1
            trial -= 1
            if trial > 0:
                # Returning how many trials left to the user to try again
                print(f"Sorry you got it wrong! You have {trial} trials.\n")
            else:
                print(
                    f"Sorry, you have run out of trials.\n The number "
                    f"I was thinking of was {guessing_number4}."
                    )
                return False


guess_step_four = guessing_game_step_four()
print(guess_step_four)


def guess_the_number():
    # 5th guessing section
    number = random.randint(1, 100)
    print("Welcome to stage 5 \n")
    print("I'm thinking of a number between 1 and 100."
          f"Can you guess what it is?")
    for i in range(10):
        guess = int(input("Guess #" + str(i+1) + ": "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(
                 "Congratulations!"
                 f"You guessed the number in " + str(i+1) + " guesses.\n"
                 )
            return
    print("Sorry, you didn't guess the number. It was " + str(number) + ".")


guess_the_number()
print("Congratulation for completing the game to the end\n")

replay_game()
print("Thanks for playing")
