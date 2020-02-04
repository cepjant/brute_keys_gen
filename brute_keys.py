import itertools
import string



def word(word, keys_len):
    if keys_len >= 1:
        for i in itertools.product(string.ascii_lowercase + string.digits + "_", repeat=1):
            f.write(word + ''.join(i) + '\n')
            f.write(''.join(i) + word + '\n')
    if keys_len >= 2:
        for i in itertools.product(string.ascii_lowercase + string.digits + "_", repeat=2):
            f.write(word + ''.join(i) + '\n')
            f.write(''.join(i) + word + '\n')
    if keys_len >= 3:
        for i in itertools.product(string.ascii_lowercase + string.digits + "_", repeat=3):
            f.write(word + ''.join(i) + '\n')
            f.write(''.join(i) + word + '\n')
    if keys_len >= 4:
        for i in itertools.product(string.ascii_lowercase + string.digits + "_", repeat=4):
            f.write(word + ''.join(i) + '\n')
            f.write(''.join(i) + word + '\n')
    if keys_len >= 5:
        for i in itertools.product(string.ascii_lowercase + string.digits + "_", repeat=5):
            f.write(word + ''.join(i) + '\n')
            f.write(''.join(i) + word + '\n')
    if keys_len >= 6:
        for i in itertools.product(string.ascii_lowercase + string.digits + "_", repeat=6):
            f.write(word + ''.join(i) + '\n')
            f.write(''.join(i) + word + '\n')


xword = input('Enter a word you want to use: ')
keys_len = int(input('What is the maximum number of characters you want to add? (1-6): '))
dpath = input("Enter a directory path to save brute keys in.\n"
            "Be careful! Make sure that there is no file named 'keys_for_brute.txt' in this directory, "
            "or it will be overwritten, \n")
if dpath[-1] == '/':
    dpath = dpath[0:-1]

fpath = dpath + '/' + 'keys_for_brute.txt'

with open(fpath, 'w') as f:
    word(xword, keys_len)

