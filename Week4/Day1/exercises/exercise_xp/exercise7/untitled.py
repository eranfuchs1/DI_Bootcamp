num = ''

while not num.isnumeric():
    num = input('enter a number: ')


if int(num) % 2 == 0:
    print('even')
else:
    print('odd')
