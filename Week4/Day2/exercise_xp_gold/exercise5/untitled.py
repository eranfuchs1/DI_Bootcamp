words = input('enter 7 words: ')
letter = input('enter a single character: ')
for word in words.split(' '):
    if letter in word:
        print(word.index(letter))
    else:
        print(f'letter doesn\'t exist in the word {word}')
