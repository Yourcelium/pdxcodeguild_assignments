#sort split replace

print('This is an anagram detector. Plug in two words to see if they match up!')

def anagram_detector():
    first_word = sorted(list(input('What is your first word\n>').lower().replace(" ","")))
    second_word = sorted(list(input('What is your second word\n>').lower().replace(" ","")))
    if first_word == second_word:
        print("Match Confirmed")
    else:
        print('No Match')
    again = input('Type \"FRICK YEAH\" to check another match, else type anything\n>').lower()
    if again == 'frick yeah':
        anagram_detector()
    else:
        print('Get outta here you shmuck!'.upper())
        exit()

anagram_detector()