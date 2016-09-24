from mysqrt import mysqrt
from tabulate import tabulate
import math

def test_square_root():
    print(repr('a').rjust(2), repr('mysqrt(a)').rjust(20), repr('math.sqrt(a)').rjust(20), repr('diff').rjust(20))
    print('--'.rjust(2), '---'.rjust(20), '---'.rjust(20), '---'.rjust(20))
    i = 1
    while i < 10:
        print(repr(i).rjust(2), repr(mysqrt(i)).rjust(20), repr(math.sqrt(i)).rjust(20), repr(abs(mysqrt(i) - math.sqrt(i))).rjust(20))
        i += 1

test_square_root()