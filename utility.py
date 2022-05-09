import re
from statistics import median


def count_words(text_string):
    dictionary = {}
    print(text_string)
    re_words = re.findall(r'\b\w{1,20}\b', text_string)

    for word in re_words:
        count = dictionary.get(word, 0)
        dictionary[word] = count + 1

    dictionary_keys = dictionary.keys()
    summ = 0

    for words in dictionary_keys:
        print(words, dictionary[words])
        summ += dictionary[words]

    print(summ)

    return summ


def get_average_sentence_size(text_string):
    print('\n')
    # for strs in text_string:
    re_words = (re.split(r'[\.\?!]', text_string))
    # '*[\.\?!][\'"\)\]]* *'
    re_words.pop()
    # last \n making a new sentence
    print("sentences are : ", re_words)
    print("count of sentences is :", len(re_words))

    print("median = ", median([len(re.findall(r'\b\w{1,20}\b', sentence)) for sentence in re_words]))

    return len(re_words)


def find_n_gram(text_string):
    dictionary = {}

    top_count = int(input("Input K - count of most popular N-gram "))
    word_count = input("Input N-gram ")

    pattern = r'\b\w{'+word_count+'}\\b'
    re_words = re.findall(pattern, text_string)

    for word in re_words:
        count = dictionary.get(word, 0)
        dictionary[word] = count + 1

    dictionary_value = list(dictionary.items())
    dictionary_value.sort(key=lambda i: i[1])
    dictionary_value.reverse()

    count = 0
    while count < top_count and count != len(dictionary_value):
        print(dictionary_value[count])
        count += 1
