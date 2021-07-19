def list_concat(a, b):
    answer = []
    for item in a:
        answer.append(item)
    for item in b:
        answer.append(item)
    return answer
print(list_concat([1,2,3], [4,5,6]))
