import random
word = 'hello'
hidden = '*****'
guessed_letter = 'l'
hidden = ''.join(map(lambda l: guessed_letter if l[0] == guessed_letter else l[1], zip(word, hidden)))
guessed_letter = 'h'
hidden = ''.join(map(lambda l: guessed_letter if l[0] == guessed_letter else l[1], zip(word, hidden)))
print(hidden)

bodypart = ''.join(chr(random.randint(97,122)) for _ in range(100))

print('''
  {}
 {} {}
 {}{}{}
 {} {}  {}
 {} {}   {}{}{}
 {}{}{}
 {} {}           {}
 {}{}{}{}{}
'''.format(*bodypart))

