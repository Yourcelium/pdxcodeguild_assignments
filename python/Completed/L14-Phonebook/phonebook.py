"""
    This is a phone book to store contact names, numbers, and notes.

"""

phonebook = {'aubre': {'name': 'Aubre',
                        'number': 5555555555,
                        'phrase': 'Very important Number'},
            'police': {'name': 'Portland Police',
                        'number':5038230000,
                        'phrase': 'Call incase of emergency'}}

def create_new_contact(name, number, phrase):
    name = input('\nWhat would you like your contact name to be?\n>'.lower())
    number = int(input('\nWhat would you like your contact number to be?\n>'.lower()))
    phrase = input('\nWhat would you like your contact phrase to be?\n>'.lower())
    phonebook[name]= {'name': name, 'number': number,'phrase': phrase}

def search_name():
    contact = input('\nWhat name would you like me to search by?\n').lower()
    if contact in phonebook:
        print('\n{}\n'.format(phonebook[contact]))
    else:
        a = input('\nI cant find that, would you like me to put that in?(Y/N)\n>'.lower())
        if a == 'y':
            n = input('\nWhat would you like your contact name to be?\n>'.lower())
            num = int(input('\nWhat would you like your contact number to be?\n>'.lower()))
            p = input('\nWhat would you like your contact phrase to be?\n>'.lower())
            create_new_contact(n,num,p)
        else:
            print("\nOk\n")

def search_num(number):
    results_lst = []
    str_num = input('\nWhat number would you like me to look up?\n>\n')
    for name, dictionary in phonebook.items():
        if str_num in str(dictonary[number]).lower():
            results_lst.append((name, dictionary))
    if len(results_lst) > 0:
        print('Found {} with the number {}'.format(len(results_lst),number))
        for i in range(len(results_lst)):
            print("\n\nname: {}\nNumber:{}\nPhrase:{}\n".format(results_list[i][1]['name'], results_list[i][1]['number'], results_list[i][1]['phrase']))


def search():
    options = {'name' : search_name, 'number': search_num}
    query = input("Would you like to search by name or number\n".lower())
    if query in options:
        options[query]()
    else:
        print('\nI don\'t understand\n')
        search()
    phonebook_go(phonebook)

def update_contact(name, num, phrase):
    delete_contact(name)
    create_new_contact(name, num, phrase)
    phonebook_go(phonebook)


def delete_contact(contact):
    if contact in phonebook:
        deleted = phonebook.pop(contact, None)
        print('You have deleted {}'.format(deleted))
    else:
        print("I dont show that contact in my phonebook")
    phonebook_go(phonebook)


def phonebook_go(phonebook):
    a = input('1: Add\n'
                      '2: Search\n'
                      '3: Edit\n'
                      '4: Remove\n'
                      'Type exit to quit.\n>: '.lower())
    if a == "1":
        n = input('\nWhat would you like your contact name to be?\n>'.lower())
        num = int(input('\nWhat would you like your contact number to be?\n>'.lower()))
        p = input('\nWhat would you like your contact phrase to be?\n>'.lower())
        create_new_contact(n,num,p)
    elif a == "2":
        search()
    elif a == "3":
        oldname = input('\nWho would you like to update\n>'.lower())
        new_num = input('\nWhat would you like the number to read?\n>'.lower())
        phrase = input('\nWhat would you like the phrase to read?'.lower())
        update_contact(oldname,new_num,phrase)
    elif a == "4":
        c = input('\nWhich contact would you like to delete\n>'.lower())
        delete_contact(c)
    elif a == 'exit':
        print('Goodbye!')
        exit()
    else:
        print('\nSorry I didn\'t undestand that\n')
        phonebook_go(phonebook)

phonebook_go(phonebook)
