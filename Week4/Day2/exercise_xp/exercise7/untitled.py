answer = '['
for key, val in enumerate(list([1,2,3,4,5,6,7])):
    if key % 2 == 0:
        answer += f'{val},'
answer = answer.rstrip(',')
answer += ']'
print(answer)

