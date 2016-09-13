
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

input()