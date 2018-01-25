word_count = {}

text = open('Alice_Adventure.txt', 'r')

text_list = text.read()

translator = str.maketrans('', '', string.punctuation)

clean_text_list = text_list.translate(translator)

word_list = clean_text_list.split()


for word in word_list:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

word_count_lst = word_count.items()

sorted_lst = list(reversed(sorted(word_count_lst,key=itemgetter(1))))


print(sorted_lst[0:10])