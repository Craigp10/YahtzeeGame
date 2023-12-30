# Yahtzee

This is a OOP Yahtzee game developed via python
Besides the basic of programming everything I used
in Python is self taught. So I'm constantly coming back and improving the program. If you find any improvements to make, feel free to contact me!

### Task

Build OOP styled Yahtzee game to understand the fundamentals of Object Oriented Programming

### Inspiration

I initially built this yahtzee game after learning the basics of python, and quickly learned the advantages to working with classes from issues I faced while developing.

### Summary

This is a command line python program and that can be played with any number of players. It follows the typical Yahtzee game. Players enter their name at the start, and take turns rolling dice and picking scores based on their dice rolled. After the number of turns decided at the beginning, a winner will be calculated!

#### To run locally

- Run this command: git clone `https://github.com/Craigp10/YahtzeeGame.git`

- cd into the directory 'YahtzeeGame'

- Insure python or python3 is installed localled and run this command: `python3 game_manager.py`

- Happy playing!!

### Game Flow

1. Enter the names of players playing. At least 1 player up to 4 players

- Need their first name with a space inbetween players, ex `> Craig Cam`

2. Enter a number for the number of rounds you wish to play, atleast 1 up to 13.

- Ex `> 12`

3. Begin playing rounds

- Each round follows a structure like:

1. Dice is rolled.
2. Player can make decision to make a score, or re roll dice for up to 2 re roll rounds.
3. A player can make a score by typing in the name of the score.
4. The round continues to the rest of the players and repeats steps 1 - 3 above.
5. After the # of specified rounds have been played a winner is decided based on score.
6. Game is now over.

### Tech Stack

Python
