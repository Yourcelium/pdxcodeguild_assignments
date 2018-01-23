from random import randint

print("""

                                 Welcome!
     When you are ready please think of a number, then type another number
  that is larger than that number. Then I will try to guess your first number

""")


start = int(input("Type your number here\n>"))

ready = input("\nWhen you have thought of a number between 1 and and {} type anything\n>".format(start))
correct = False
high_limit = start
low_limit = 1
while correct == False:
    guess = randint(low_limit,high_limit)
    answer = input("\nYour number is {}, Correct? (Y/N)\n>".format(guess)).lower()
    if answer == "y":
        print ("\nMaschines rule! People Drool\n")
        correct = True
    if answer == "n":
        hint = input("\nWas my guess high or low\n>").lower()
        if hint == "high":
            high_limit = guess - 1
            hint = ''
        elif hint == "low":
            low_limit = guess + 1
            hint = ''
print("\n\nPleasure playing with you\n\n")
