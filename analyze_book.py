import random
import string

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        # INSERT CODE BELOW
        for word in line.split():
            word = word.strip(string.whitespace)
            word = word.strip(string.punctuation)
            word = word.lower()

            # Update the histogram
            hist[word] = hist.get(word,0) + 1

    return hist




def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

# Testing
hist = process_file('kamasutra.txt', skip_header = False)
#print(hist)

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

# Testing
# print(total_words(hist))

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist.keys())

# Testing
# print(different_words(hist))

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, freq in hist.items():
        temp.append((freq, word))

    temp.sort()
    temp.reverse()
    return temp

# Testing
# common = most_common(hist)
# print(common[:20])

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    temp = []
    for word, freq in hist.items():
        temp.append((freq, word))

    temp.sort()
    temp.reverse()
    print(temp[:num])

# Testing
# print_most_common(hist, 20)

def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    result = dict()
    for i in d1:
        if i not in d2:
            result[i] = d1[i]
    return result

# Testing 
# test1 = {'a':1, 'b':2, 'c':3, 'd':4}
# test2 = {'a':2, 'b':2, 'e':5}
# print(subtract(test1, test2))

def subtract_words(d1,d2):
    '''
    d1, d2: Dictionaries
    d1 is the histogram of wordsin the textfile
    d2 is the word list to compare against
    '''
    print(subtract(d1,d2))

# Testing
# wordlist = process_file('words.txt', skip_header = False)
# subtract_words(hist, wordlist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    total = total_words(hist)
    temp = []
    cumprob = 0

    for word, freq in hist.items():
        weight = cumprob + (freq/total)
        cumprob += weight
        temp.append((word, weight))

    rand = random.random()
    for word,weight in temp:
        if rand<weight:
            return word
    

    
# Testing
print(random_word(hist))


def main():
    hist = process_file('kamasutra.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


# if __name__ == '__main__':
#     main()
