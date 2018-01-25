'''
Here is how to play ‘Guess The Number’:

Display a welcome screen to the user.
The Computer chooses a random number between 1 and 2 billion.
After the computer chooses a number, the human attempts to guess the computer’s secret number in as few guesses as possible. The human:

Guessses a number
The computer will respond with a message ‘too high!’ or ‘too low!’
Repeat until the human guesses the exact number correctly.
score is kept like golf: lower is better!
'''
from random import randint

answer = randint(1,10)
guess = 0
score = 0

print("""
                   *****WELCOME TO GUESS THE NUMBER*****
                     Try to guess my beautiful number
                        Only the best will surivive
""")

while not answer == guess:
    guess = int(input("What is your guess:"))
    score = score + 1
    if answer < guess:
        print("Too High")
    elif answer > guess:
        print("Too Low")
    if score == 10:
        print("Dont give up you got this!")
    if score == 20:
        print("Wow, umm, this is sort of embarassing")

print("""
*********************************BINGO******************************************
 ******************************************************************************
********************************************************************************
 ******************************************************************************
                    Your score was {}. Try to do better!"
                                Goodbye
""".format(score))
