from random import choice

print("This is a magic eight ball!")

fortunes = ['You will go to sleep at some point tonight', 'You will need to drink water at some point in the forseeable'
                                                          'future', 'Your life will soon revolve around cheese']


def magic8ball():
    shake = input('For a prediction into your future, type shake\n>').lower()
    if shake == 'shake':
        print(choice(fortunes))
        again = input('Do you wanna go again? Type \"I love to shake it\" to get another fortune\n>').lower()
        if again == "i love to shake it":
            magic8ball()
        else:
            print('Buh Bye')
            exit()

    else:
        print('i said shake you dummy'.upper)
        magic8ball()

magic8ball()