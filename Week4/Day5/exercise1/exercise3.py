lowers, uppers = 0, 0
for i in map(lambda l: 1 if l.isupper() else 2 if l.islower() else 0, input()):
    if i == 1:
        uppers += 1
    elif i == 2:
        lowers += 1
print(f'number of lowercase letters: {lowers}, number of uppercase letters: {uppers}')
