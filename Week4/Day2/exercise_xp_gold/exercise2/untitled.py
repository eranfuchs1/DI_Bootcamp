biggest = 0
for key, num in enumerate([int(input(f'input number({3 - i} left to input): ')) for i in range(0, 3)]):
    if key == 0:
        biggest = num
    elif num > biggest:
        biggest = num
print(biggest)
