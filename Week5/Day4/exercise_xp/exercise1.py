from random import choice
from sys import argv


def get_words_from_file(f):
    return list(map(lambda word: word[:-1], f.readlines()))

def get_random_sentence(length=10):
    global wlist
    return ' '.join([choice(wlist) for _ in range(length)]).capitalize() + '.'

with open('sowpods.txt', 'r') as f:
    wlist = get_words_from_file(f)
    print(get_random_sentence(int(argv[1])) if len(argv) > 1 and argv[1].isnumeric() else get_random_sentence())
