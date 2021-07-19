num = int(input('input a number from 1 to 9 (including): '))
import random

if random.randint(1,9) == num:
    print('winner')
else:
    print('better luck next time')
