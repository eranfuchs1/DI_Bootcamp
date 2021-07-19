alphabet = [chr(i) for i in range(65, 91)]

for l in alphabet:
    if l in 'AEIOUYW':
        print(f'{l} is a vowel')
    else:
        print(f'{l} is a consonant')
