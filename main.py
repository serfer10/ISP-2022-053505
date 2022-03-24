import utility


def main():
    text = open('Text', 'r')
    text_string = text.read().lower()
    text.close()

    words = utility.count_words(text_string)
    sen = utility.get_average_sentence_size(text_string)
    print("word on a sentence = ", words / sen)
    utility.find_n_gram(text_string)


main()
