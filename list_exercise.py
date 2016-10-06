def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for i in t:
        total += sum(i)
    return total


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    total = 0
    result = list()
    for i in t:
        total += i
        result.append(total)
    return result


def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return t[1:len(t)-1]



def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t.pop()
    t.pop(0)
    return t


def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    for i in range(1,len(t)):
        if t[i] < t[i-1]:
            return False
    return True


def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    if len(word1)==len(word2):
        i = 0
        j = len(word2)-1
        while j >= 0:
            if word1[i] != word2[j]:
                return False
            i = i + 1
            j = j - 1
        return True
    else:
        return False


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool
    """
    for i in s:
        if s.count(i)>1:
            return True
    return False

def has_adjacent_duplicates(s):
    """Returns True if any element appears more than once consecutively in a sequence.

    s: string or list

    returns: bool
    """
    before = s[0]
    for i in s[1:]:
        if i == before:
            return True
        else:
            before = i
    return False



def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

    print(has_adjacent_duplicates('abba'))
    print(has_adjacent_duplicates('abab'))


if __name__ == '__main__':
    main()
