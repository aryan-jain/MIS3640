from inlist import make_word_list, in_bisect


def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    word1 = word[1::2]
    word2 = word[0::2]
    if in_bisect(word_list,word1) and in_bisect(word_list, word2):
        return True


def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    words = []
    for i in range(0,n-1,1):
        words.append(word[i::n])
    for j in words:
        if not in_bisect(word_list, j):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
