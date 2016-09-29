fin = open('words.txt')
line = repr(fin.readline())
# https://docs.python.org/3/library/functions.html#repr

fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    print(word)


def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

read_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    a = word.strip()
    flag = False
    for letter in a:
        if letter == 'e' or letter == 'E':
            flag = True
    if not flag:
        return False
    else:
        return True
print('has_no_e')
print(has_no_e('Epicenter'))
print(has_no_e('Ex'))
print(has_no_e('Ball'))

def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for i in word:
        for j in forbidden:
            if(i == j):
                return False
    return True
print('avoids')
print(avoids('elephant', 'iao'))
print(avoids('mother', 'cfk'))

def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    flag = False
    for i in word:
        if i not in available:
            return False
    return True


print('uses_only')
print(uses_only('father', 'arthe'))
print(uses_only('mother', 'thermo'))
print('hello, call of face halo.')


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for i in required:
        if i not in word:
            return False
    return True

print('uses_all')
print(uses_all('father', 'arthe'))
print(uses_all('mother', 'thermoz'))

def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for i in word:
        if i.lower() < before.lower():
            return False
        before = i
    return True

print('is_abecedarian')
print(is_abecedarian('abel'))
print(is_abecedarian('able'))

def is_alphabetical(word):
    """
    Recursive version of is_abecedarian function.
    """
    if word[1].lower() < word[0].lower():
        return False
    else:
        is_alphabetical(word[1:len(word)-1])
    return True

print('is_alphabetical')
print(is_abecedarian('abel'))
print(is_abecedarian('able'))
        