# phonebook = [
#     ('jones', {
#         'f_name': 'Chris',
#         'l_name': 'Jones',
#         'number': 5032779710
#     }),
#     ('dover', {
#         'f_name': 'Sheri',
#         'l_name': 'Dover',
#         'number': 5032779710
#     })
# ]

phonebook = {
    'jones': {
        'f_name': 'Chris',
        'l_name': 'Jones',
        'number': 5032779710
    },
    'dover': {
        'f_name': 'Sheri',
        'l_name': 'Dover',
        'number': 5036025412
    }
}


# Create New Contact
def create(f_name, l_name, number):
    if l_name not in phonebook:
        phonebook[l_name.lower()] = {'f_name': f_name, 'l_name': l_name, 'number': number}
    else:
        print('{} {} is already in the phonebook!'.format(f_name, l_name))


# Retrieve Contact
def search_f_name(name):
    results_list = []
    for last_name_key, dictionary in phonebook.items():
        if name in dictionary['f_name'].lower():
            results_list.append((last_name_key, dictionary))
    if len(results_list) > 0:
        print('{} {} found:'.format(len(results_list), 'results' if len(results_list) > 1 else 'result'))
        for i in range(len(results_list)):
            print(
                "{}: {} - {}".format(i + 1, '{} {}'.format(results_list[i][1]['f_name'], results_list[i][1]['l_name']),
                                     results_list[i][1]['number']))


def search_l_name(name):
    results_list = []
    for last_name_key, dictionary in phonebook.items():
        if name in dictionary['l_name'].lower():
            results_list.append((last_name_key, dictionary))
    if len(results_list) > 0:
        print('{} {} found:'.format(len(results_list), 'results' if len(results_list) > 1 else 'result'))
        for i in range(len(results_list)):
            print(
                "{}: {} - {}".format(i + 1, '{} {}'.format(results_list[i][1]['f_name'], results_list[i][1]['l_name']),
                                     results_list[i][1]['number']))


def search_number(number):
    string_number = str(number)
    results_list = []
    for last_name_key, dictionary in phonebook.items():
        if string_number in str(dictionary['number']).lower():
            results_list.append((last_name_key, dictionary))
    if len(results_list) > 0:
        print('{} {} found:'.format(len(results_list), 'results' if len(results_list) > 1 else 'result'))
        for i in range(len(results_list)):
            print(
                "{}: {} - {}".format(i + 1,'{} {}'.format(results_list[i][1]['f_name'], results_list[i][1]['l_name']),
                                     results_list[i][1]['number']))


def search():
    options = {'first_name': search_f_name, 'last_name': search_l_name, 'number': search_number}
    query = input("Would you like to search by first name, last name or number\n>: ").lower()
    if query.replace(' ', "_") in options:
        query2 = input("What is the {} you would like to search by?\n>: ".format(query)).lower()
        options[query.replace(' ', "_")](query2)
    else:
        print('I did not understand that.')
        # name = input("Enter the last name of the person you are looking for.\n>: ").lower()
        #
        # if name in phonebook:
        #     print(phonebook[name]['f_name'])
        #     print(phonebook[name]['l_name'])
        #     print(phonebook[name]['number'])
        # else:
        #     query = input('I can\'t find anyone by that name. Would you like to create a contact? (y/n)').lower()
        #     if query in 'yes':
        #         f = input("Enter the first name of the person you are adding.\n>: ")
        #         last = input("Enter the last name of the person you are adding.\n>: ")
        #         n = input("Enter the phone number of the person you are adding.\n>: ")
        #         create(f, last, n)
        #     elif query in 'no':
        #         return None
        #     else:
        #         print('I don\'t understand you...')


# Update Existing Contact
def update(old_l_name, f_name, l_name, number):
    delete(old_l_name)
    create(f_name, l_name, number)


# Delete Contact
def delete(name):
    if name in phonebook:
        del phonebook[name]
    else:
        print('I can not find anyone by that name.')


if __name__ == "__main__":
    # search_f_name('s')
    # search_l_name('s')
    # search_number('7')
    while True:
        query = input('1: Search\n'
                      '2: Add\n'
                      '3: Edit\n'
                      '4: Remove\n'
                      'Type exit to quit.\n>: ').lower()
        if query == '1':
            search()
        elif query == '2':
            f = input("Enter the first name of the person you are adding.\n>: ")
            last = input("Enter the last name of the person you are adding.\n>: ")
            n = input("Enter the phone number of the person you are adding.\n>: ")
            create(f, last, n)
        elif query == '3':
            old_l_name = input('Please enter the old last name of the person you are changing\n>: ').lower()
            f_name = input('Please enter the new first name of the person you are changing\n>: ')
            l_name = input('Please enter the new last name of the person you are changing\n>: ')
            number = input('Please enter the new number of the person you are changing\n>: ')
            update(old_l_name, f_name, l_name, number)
        elif query == '4':
            na = input("Enter the last name of the person you would like to remove.\n>: ")
            delete(na)
        elif query == 'exit':
            exit()
        else:
            print("I'm sorry, I can not do that right now.")
