"""
    This is a phone book to store contact names, numbers, and notes.
"""

phonebook = {'aubre': {'name': 'Aubre',
                        'number': 5555555555,
                        'phrase': 'Very important Number'},
            'police': {'name': 'Portland Police',
                        'number':5038230000,
                        'phrase': 'Call incase of emergency'}}

def create_new_contact():
    name = input('\nWhat would you like your contact name to be?\n>')
    number = int(input('\nWhat would you like your contact number to be?\n>'))
    phrase = input('\nWhat would you like your contact phrase to be?\n>')
    phonebook[name]= {'name': name,
                        'number': number,
                        'phrase': phrase}
# def retrieve_contact():
#     contact = input("\nWhat contact would you like me to retrieve?\n>".lower())
#     if contact in phonebook:
#         print(phonebook[contact])
#     else:
#         a = input('\nI cant find that, would you like me to put that in?(Y/N)\n>'.lower)
#         if a == 'y':
#             create_new_contact()
#         else:
#             print("\nOk\n")

def partial_contact_retrive(partial):
    tup_phonebook = phonebook.items()
    for i[0] in tup_phonebook:
        if partial in i[0]:


def update_contact():
    contact = input('\nWhich contact would you like updated?\n>'.lower())
    update = input('\nWould you like to update NAME, NUMBER, or PHRASE?'.lower())
    new_info = input('\nWhat would you like it to say?\n>')
    if update == 'name':
        phonebook[contact['name']] = new_info
    elif update == 'number':
        phonebook[contact['number']] = int(new_info)
    elif update == 'phrase':
        phonebook[contact['phrase']] = new_info

def delete_contact():
    contact = input('\nWhich contact would you like to delete\n>')
    if contact in phonebook:
        deleted = phonebook.pop(contact, None)
        print('You have deleted {}'.format(deleted))
    else:
        print("I dont show that contact in my phonebook")
def phonebook_go(phonebook):
    a = input('How can I help you?'.lower())
    if a == "create contact":
        create_new_contact()
    elif a == "retrieve contact":
        retrieve_contact()
    elif a == "update contact":
        update_contact()
    elif a == "delete_contact":
        delete_contact()
    else:
        print('Sorry I didn\'t undestand that')

phonebook_go(phonebook)
