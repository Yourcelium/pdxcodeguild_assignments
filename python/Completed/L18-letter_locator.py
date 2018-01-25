print('This program finds where a letter occurs within a statement, or returns a -1 if it does not occur at all\n\n')


def find_letter():
    phrase = input("Which phrase are we working with?\n>")
    letter = input("And what is the letter?\n>")
    index_lst = []
    while len(letter) > 1:
        print('Wow there buddy. Please just type a letter')
        letter = input("Ok, lets try this again, type a LETTER\n>")
    start = 0
    while True:
        index = phrase.find(letter, start)
        if index == -1:
            break
        else:
            index_lst.append(index)
        start = int(index) + 1
    if len(index_lst) == 0:
        index_lst.append(-1)
    print(index_lst)
    return index_lst

find_letter()