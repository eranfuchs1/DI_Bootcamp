def angles(content):
    return ''.join([''.join([content[i * 3  + (-1 if _ < 0 else 1)*(_ + i)] for i in range(3)]) + ' ' for _ in [0,-2]])

def columns(content):
    return ''.join([''.join([content[l * 3 + i] for l in range(3)]) + ' ' for i in range(3)])

def check_over(content):
    result = f"{content} {angles(content)} {columns(content)}"
    print(result)
    return 1 if 'xxx' in result else 2 if 'ooo' in result else 0

content = ' ' * 9
template = '''
*****************************
*                           *
*                           *
*         |      |          *
*       {} |   {}  |  {}       *
*         |      |          *
*     ----+------+-----     *
*         |      |          *
*       {} |   {}  |  {}       *
*         |      |          *
*     ----+------+-----     *
*         |      |          *
*       {} |   {}  |  {}       *
*         |      |          *
*                           *
*                           *
*****************************
'''


for i in range(9):
    symbol = 'x' if i % 2 == 0 else 'o'
    print(f"{symbol}'s turn")
    col, row = None, None
    while True:
        col, row = map(lambda l: int(l) ,input('pos (<col> <row>):').split(' '))
        if content[3 * row + col] == ' ':
            break
        else:
            print('spot already taken!')
    content = f"{content[:3 * row + col]}{symbol}{content[3 * row + col + 1:]}"
    print(template.format(*content))
    over = check_over(content)
    print('x won\n' if over == 1 else 'o won\n' if over == 2 else '', end="")
    if over:
        break
