# Guess The Number
Welcome to guess the number game, a very easy and quick start game for new user.
This is a game were the player have to guess the correct number, maybe 
between 0 to 5 or 1 to 10...depend on what stage. And in each stage the player have 
some amount of trials to keep guessing, and if he run out of trial the correct number
will be print out to the player
[Link to the live website](https://guessingthenumber-4cd80cfa8d4d.herokuapp.com/)
![Screenshot (168)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/b7ceb541-85bb-41c0-9622-228a79d91c21)

## Features
#### Do you already have an account
This is the first board of the game. This section require to you to select either Y or N to know if
you are already an existing user or not, If Y..then it ask you to input your username and passowrd, then 
a welcome back message will be print to the terminal. But if N, you have to sign up to become a user.
![Do you already have an account (170)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/a29c518d-1ac2-48a4-95aa-c59e4f6d9359)

#### Log in
This section allow the users to log in, into there existing account if they choose Y
![Screenshot (174)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/5ff6ad8a-8641-4585-a0d8-edd2afb0a2f1)

#### Sign up
This section allow's users to sign up...if they choose N. They will have to sign up if they don't have an existing account.
![Screenshot (175)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/0c2c409c-a5a9-405d-b125-fdbc64aa4991)


#### Initializing...! Starting game in process...
This section is a quick one, I thought this was also interesting to add some more flexible functionalities
to the game from the little experience i have as i keep growing to be better with python. This section doesn't
require for a second sign up but only ask for your sign up name.
![Screenshot (171)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/54ea876f-f94d-4dbe-bfc6-fe3f69f35a5e)

#### Loading Game...
Another functionality that i also thought that would make sense, was to also add a loading game seconds 
before the game start as the user prepare. This section is a countdown seconds from 10 to 0, then the main game begins.
![Screenshot (172)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/4e7a4e83-726d-43ae-83a0-cb824ef2eb45)

#### I'm thinking of a number from 0 to 5
This section is the very beginning of the game after users input or log in or sign up. With this very
beginning the user have 2 trials to guess the number correct, and if he get it wrong, on the terminal, there will 
be printed out how many trials left and he will have to try again, and if he run out of trials, on the terminal, there will
be printed out the random number. That how each stage of the game goes till he plays to the end.
![Screenshot (173)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/895936b7-2914-4b43-81a0-ba89681e342e)

#### Would you like to restart the game?
This section allow's the users to select one option, after playing to the end of the game...either Y or N if they decided, they want
to play again from the beginning
![Screenshot (176)](https://github.com/Elvisthegreat/Rock-paper-scissors/assets/141064225/190279bf-8fe9-4fb7-9939-5f840f39d10a)

## Project Goals
### Users Stories
* To be able to play guess the number
* To be able to have the flexibility of the game
* To be able to sign up
* To be able to play without bugs stress
* To be able to restart game after playing to the end
* To be able to log in with their signed up name without having to register again with new name

### Site Owner Goal
* Create a game that is easy for the user to play
* Create a game that is easy for the user to understand
* Create an option that allow the user to sign in
* Create an option that allow the user to login
* Create a game from my knowledge and want to know what the user think about the the game
* Make sure user can restart or exit the game when they play to the end

### User Experience
From what i learned from (UX). I make sure i use a simple and understandable english in a way
users can easily read and get the the point of the game for i am creating a game not for myself
but for others. So users experience is something i consider very important while making the
first move for creating this game.

### Targeted Audience
* People who are looking for a simple and fun game
* People whom just want to play a game that doesn't include violence
* People who also want to be good at guessing

## Design Choices
This game was designed in a way of making things easily understandable! Something simple, fun and easy to play and understand. 
From the little knowledge i have, i tried to create something i could...making it very easy and simple especially for the
target audience.

## Language Used For This Project
* Python
### Other Technologies Used For This Project
* Microsoft Bing
   * This was used to know how to arrange some my codes that i couldn't figure out by myself
   * It was also one of the main tools i used alot to searched out some codes. like makin the
   user log in and sign up work properly and storing users details in the database e.g Dictionary
   * And the last code for the guessing game was from the micrsoft bing searches carried out. This below <br>

   def guess_the_number():<br>
    number = random.randint(1, 100)<br>
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")<br>
    for i in range(10):<br>
        guess = int(input("Guess #" + str(i+1) + ": "))<br>
        if guess < number:<br>
            print("Too low!")<br>
        elif guess > number:<br>
            print("Too high!")<br>
        else:<br>
            print("Congratulations! You guessed the number in " + str(i+1) + " guesses.")<br>
            return<br>
    print("Sorry, you didn't guess the number. It was " + str(number) + ".")<br>

guess_the_number()

## Testing
#### Bugs
* When i first deployed the project, i found out that..the Sign up section wasn't working 
as expected
* After users sign up, its wasn't breaking out from the loop, meaning...it kept asking users to sign
after they already did
* After deployment, i found the users{} dictionary wasn't storing user details after sign up
* After deployment, i found the restart game function wasn't working as expected, it didn't break out from the loop, 
that was because, where i wanted the game to start from wasn't added inside the restart game function

#### Fixed Bugs
* The Sign up
* The users{} storage dictionary
* The restart game

# Deployment

 This website was deploy with GitHub
[Guess The Number](https://guessingthenumber-4cd80cfa8d4d.herokuapp.com/)

#### How to deploy with github <br>

  1. In the GitHub repository <br>
  2. Scroll halfway down, on the right side of your screen<br>
  3. Click on github-pages
  4. A list of all lastest commit will appear, then click on the following commit you want to deploy

#### For the source 
1.select Branch: master <br>
2.After the webpage refreshes automaticaly you will see a ribbon on the top saying: Your site is published

##### You can for fork the repository by following these steps:
1.Go to the GitHub repository <br>
2.Click on Fork button in upper right hand corner <br>

##### To clone the repository by following these steps:
1.Go to the GitHub repository <br>
2.Locate the Code button above the list of files and click it <br>
3.Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard 
Open Git Bash <br>
4.Change the current working directory to the one where you want the cloned directory <br>
5.Type git clone and paste the URL from the clipboard <br>
6.Press Enter to create your local clone. <br>

