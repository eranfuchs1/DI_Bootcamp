string = input('enter a string: ')
while len(string) != 10:
    if len(string) < 10:
        string = input('string too small, try again: ')
    else:
        string = input('string too big, try again: ')


print(string[0], string[-1])

for i in range(len(string)):
    print(string[0:i + 1])

string = f"{string[0]}{string[5:0:-1]}{string[-1:5:-1]}"
print(string)
