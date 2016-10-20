import os

fout = open('output.txt', 'w')

line1 = "How many roads must a man walk down\n"
fout.write(line1)

line2 = "Before you call him a man?\n"
fout.write(line2)

# When you are done writing, you should close the file.
fout.close()
# If you don’t close the file, 
# it gets closed for you when the program ends.

print(os.path.exists('output.txt'))

# def walk(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

def walk2(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    count = 0
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))
            count += 1
    print(count, 'files in this directory')

# walk2(os.getcwd())

try:
    f_in = open('bad_file')
except: 
    print('Something went wrong here')

print('This code still works.')