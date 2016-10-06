def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    low = 0
    high = len(word_list)-1
    while low<=high:
        i = (low + high)//2
        if word == word_list[i]:
            return i
        if word < word_list[i]:
            high = i-1
        elif word > word_list[i]:
            low = i+1


if __name__ == '__main__':
    word_list = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))
