names = [name for name in input('enter your names seperated by whitespace: ').split(' ')]

names = set([name * flag for flag, name in zip([age >= 16 for age in [int(input(f'age of {name}? ')) for name in names]], names)])
names.remove('')
names = list(names)

print(names)
