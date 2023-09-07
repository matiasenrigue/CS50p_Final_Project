# TENNIS GAME SCOREBOARD
    

#### Video Demo:  
<https://www.youtube.com/watch?v=EWL5XGW9uDU&ab_channel=Mat%C3%ADasEnrigue>
  


## Project Description

This project keeps track of the score for a tennis match between two players. The scoreboard updates live as buttons are clicked to increment the scores. 

In this version its use would be to count to points of a game being played in real life and use the scoreboard to display the current score. 
The user will receive a prompt asking if a point was scored by player 1 or player 2. Based on the input the score will be incremented for the respective player and displayed on the scoreboard. 
The counting system is like in traditional tennis: 
- points (0, 15, 30, 40, Adv, Game) 
- games (0,1,2,3,4,5,6 and if necessary a tie-break) 
- sets (1 or 2, if we wanted to track mens Grand Slam matches we would need to add an option for a game played up to 3 sets won)

#### Future Versions

In future versions it could be used to also store the data of the match and display stats like total games won, aces, double faults etc. 
To make that possible we would need to add additional buttons/inputs to track different scoring events and differentiate when a player is at the service or at the return. 
Doing that would maybe require to build a GUI for the user to be more comfortable tracking a real match (introducing buttons like "Ace", "Double Fault", "Backhand Winner", "Unforced Error", etc..).

It could also be connected to an API to fetch live match data. 
Or going even further we could use it to simulate tennis matches based on past performances from our data. 
This would be way more complex since we would have to asses probabilities for different shot outcomes based on player stats, but it could be a fun project!


## Files

1. project.py
This file contains the main code for the tennis scoring game. It includes functions for getting player names, scoring points, and tracking the progress of the match. The code is more than 300 lines long, but I guess it could be reduced by using classes and obviously by reducing the commens and the spacing.

2. test_project.py
This file contains test functions for the project.py file using the unittest module. This allows testing different scoring scenarios and edge cases to ensure the scoring logic works as expected. 
As our main file requires the entrance of input this code need to be run with the following sintax:
> pytest -s test_project.py

When asked to put an input run:
- You are going to get reprompted unless you enter 2 valid names (less than 22 characters, no numbers)
- When asked: "Are you sure to exit? write "yes" or "no":" --> write "yes"

3. README.md
This file you are currently reading provides information about the project, its functionality, and how to use it. It also explains the purpose of each code file and any important design choices made during development.


### Used Packages

> import sys

> from tabulate import tabulate

> from termcolor import colored


# Hot To Use It

The program uses a console-based user interface to provide a simple and straightforward way to play the game.

Enter the names of the two players when prompted. The program will validate the names and ensure they meet the required criteria:
- Name not longer than 22 characters, which is enough to play if your name is "Félix Auger-Aliassime" but also donesnt jeopardize the general looking of the code
- Name contains only letters, no numbers are allowed to avoid confusion when reading scores
-  The names will be properly formatted by the program for visibility purposes

Then the program will start tracking the score. 
You will be prompted to enter "1" or "2" to indicate which player scored the point. The score will update after each input. 
If you enter "d" you will have the option to exit the programe (you have to confirm just in case it was accidental). 
Any other input will not be accepted.

The scoring system follows standard tennis rules, including deuce and tiebreaks.




## Design Choices

I first wanted to write this code using clases, but I realized I'm not confortable enough to do so yet, but I would like to update it in the future if I find the time to do so. 

I decided to go with functions that pass arguments between eachother. 
We first have the name part of the program which consist in a function for prompting the user, and another one for validating the name

More interesting, we have the whole game functions:
We have a infinite loop that is constantly asking for the user for input, until the user exits or the match finishes.
1. Function point_scored: We first have a function that reads the input and decides to give a point to player 1 or player 2 (or exit the code). This function returns a tupple (1,0) if player 1 won the point, or (0,1) if player 2 won
2. Function game_counter: This functions receive those tupples and adds the results to a player count. It will also be the function in charge of stopping the game when a player scores 4 points and has at least 2 point difference with his rival.
3. Function print_score: This function will be printing the score every time a point is scored. It uses the tabulate module so the output is easier to read
4. Function point_converter: This function will be converting the points from numerical system (0,1,2,3,4,5..) to tenis system (0,15,30,40,Adv, Game)

This four functions seem obvious when explained, but they were the main problem when writting the code, following the  scoring rules and using tenis scoring system while also presenting a readable output for the user. 
Once this was done the next is easier

5. Function set_counter: counts the games won by each player in a set and returns the set winner
6. Function tie_breakcounter: is launched by set_counter when both players are on tied 6 games to 6. Again it will return the winner of the tie break if a user reaches 7 points at least and has a 2 points difference with his rival.
7. Function match_counter: will count the sets won and determine the winner of the game.

After every point played the user gets an output of the current score
After every game played the user gets a different output where he sees games and sets won by each player
Tiebreaks and deuces have special graphics to make them highlight

I also used the termcolor module to make the output better looking



