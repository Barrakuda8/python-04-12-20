
user_words = input("Введите слова через пробел: ")

user_words_split = user_words.split()

for ind, word in enumerate(user_words_split):
    if len(word) > 10:
        print(ind + 1, word[:10])
        continue
    else:
        print(ind + 1, word)



