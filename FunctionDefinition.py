
def print_lyrics():
    print("Yeezy, Yeezy, Yeezy just jumped over Jumpan.")
    print("Yeezy, Yeezy, Yeezy, I feel so accomplished,")
    print("I done talked a lot of s**t but I just did the nmubers!")

print(type(print_lyrics)) #This shows us that the object print_lyrics is defined as a function
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print("OH!")
    print_lyrics()

repeat_lyrics()

def print_twice(a):
    print(a)
    print(a)

my_name = 'Aryan Jain'

print_twice(my_name)

def cat_twice(part1, part2):
    cat = part1 + " " + part2
    print_twice(cat)

line1 = "Bing Tiddle"
line2 = "Tiddle Bang"
cat_twice(line1, line2)

def give_me_a_break():
    str1 = 'Another break'
    print("Break")
    return str1             #return terminates the function

give_me_a_break()

print(give_me_a_break())

input()