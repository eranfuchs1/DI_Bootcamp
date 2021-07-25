import sys
lines = list(sys.stdin)
sys.stdin = open("/dev/tty")
user_input = input('enter a list item(<item index>. <item>): ')
index = int(user_input.split('.')[0])
def increment_index(line):
    _ = line.split('.')
    return f'{int(_[0]) + 1}{"".join(_[1:])}'
print(f'{"".join(lines[:index])}\n{user_input}\n{"".join(map(increment_index, lines[index:]))}')
