import string
#
# alpha = string.ascii_lowercase
#
# rot_13 = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
#
# encrypt_or_decrypt = input("For encrption services type 1, for decryption services press 2\n>")
#
# input_word = input("Your word please\n> ")
#
# new_word = ''
#
# def decrypt(word):
#     new_word = ''
#     for letter in word:
#         i = alpha.index(letter)
#         new_word += rot_13[i]
#     return new_word
#
# def encrypt(word):
#     new_word = ''
#     for letter in word:
#         i = rot_13.index(letter)
#         new_word += alpha[i]
#         # print(letter)
#     return new_word
#
# if encrypt_or_decrypt == "1":
#     new_word = encrypt(input_word)
# elif encrypt_or_decrypt == "2":
#     new_word = encrypt(input_word)
# else:
#     print ("You did not follow directions. Goodbye")
#     exit()
#
# print("THIS IS YOUR ANSWER: {}".format(new_word))
word = input("Your word here")

translator = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[13:]+ string.ascii_lowercase[:13])

new_word = word.translate(translator)

print(new_word)
