import random

def display_message():
    print('I\'m learning fullstack web dev in this course.')

display_message()

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Alice in Wonderland')

def describe_city(name, country="England"):
    print(f"{name.title()} is in {country.title()}")

describe_city('tel aviv', 'israel')


def compare_random(num):
    num2 = random.randint(1,100)
    if num == num2:
        print('sucess!')
    else:
        print(f'fail! num1 : {num}, num2: {num2}')

compare_random(2)

def make_shirt(size, text):
    print(f'size: {size}, text: {text}')

make_shirt('m', 'hello world')
def make_shirt(size='l', text='I love Python'):
    print(f'size: {size}, text: {text}')
make_shirt(text='hello world', size='m')


magicians = [
        'AMASIS',
        'THE AMAZING JOHNATHAN',
        'CRISS ANGEL',
        'THEODORE ANNEMANN',
        'ANVERDI',
        'ARGUS',
        'BALABREGA',
        'CARL BALLANTINE',
        'BEN ALI BEY',
        'MOHAMMED BEY',
        ]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for index, name in enumerate(magicians):
        magicians[index] = f'the Great {name}'
    return magicians

make_great(magicians)
show_magicians(magicians)
