def is_triple_double(word):
    """
    Tests if a word contains three consecutive double letters.
    word: string
    returns: bool
    """
    if len(word)>=6:
        if word[1] == word[2]:
            if word[3] == word[4]:
                if word[5]==word[6]:
                    return True
        else:
            return is_triple_double(word[2:len(word)])
    else:
        return False

print(is_triple_double('haallss'))
print(is_triple_double('asddefr'))

def find_triple_double():
    """
    Reads a word list and prints words with triple double letters.
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')