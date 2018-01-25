def palindrome_detector():
    a = input("What is your word\n>>>".lower)
    # if len(a) % 2 == 0 and a[:(len(a)/2)] == a[:-(len(a)/2)]:
    #     return True
    # elif len(a) % 2 == 1 and a[:(len(a)/2)] == a[(:-()(len(a)/2) + 1)]:
    #     return True
    # else:
    #     return False
    a = a.replace(" ", '')
    ar = ''.join(reversed(a))

    if a == a[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')

    print('See?\n{}\n{}\n'.format(a,ar))

    again = input("would you like to play again (y/n)".lower())

    if again == 'y':
        palindrome_detector()
    else:
        print('goodbye')
        exit()



palindrome_detector()
