import csv

with open('phonebook.csv') as csvfile:
    phonebook = csv.reader(csvfile, de;o,oter = ',')

    for row in phonebook:
        print(', '.join(row))

def load_phonebook():
    pb = []
    with open('phonebook.csv', newline='') as csvfile:
        phonebook =  csv.reader(csvfile, delimiter=',')

        for row in list(phonebook)[1:]:
            pb[row[0]] = {'f_name': row[1], 'l_name': row[2, 'number': row[3]]}
            print(', '.join(row))

    return pb

if __name__ == '__main__'