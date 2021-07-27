from random import randint
from time import sleep

count = 0
width = 100
grid = [[' ' for i in range(width)] for j in range(39)]


def insert_random():
    global width, grid
    for _ in range(randint(100, 120)):
        grid[randint(0,38)][randint(0,width - 1)] = '#'


def check_alive(cell):
    return cell == '#'
def count_neighbors(i,j):
    global width
    if i < 1 or j < 1 or i > 37 or j > width - 3:
        return 0
    count = 0
    count += check_alive(grid[i][j - 1])
    count += check_alive(grid[i][j + 1])
    count += check_alive(grid[i+1][j - 1])
    count += check_alive(grid[i +1][j + 1])
    count += check_alive(grid[i-1][j - 1])
    count += check_alive(grid[i-1][j + 1])
    count += check_alive(grid[i-1][j])
    count += check_alive(grid[i+1][j])
    return count


def iteration():
    global grid, count, width
    if count % 355 == 0:
        insert_random()
    next_grid = [[' ' for i in range(width)] for j in range(39)]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            neighbors = count_neighbors(i,j)
            if cell == ' ':
                if neighbors == 3:
                    next_grid[i][j] = '#'
            else:
                if neighbors >= 2 and neighbors <= 3:
                    next_grid[i][j] = '#'
    grid = next_grid.copy()
    count += 1

while True: print(''.join([''.join(row) + '\n' for row in grid.copy()])); iteration(); 
