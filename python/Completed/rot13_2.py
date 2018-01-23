import string
word = input("Your word here").lower()

translator = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[13:]+ string.ascii_lowercase[:13])

new_word = word.translate(translator)

print(new_word)
