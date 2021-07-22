def compare_str(a, b):
    for l1, l2 in zip(a,b):
        if l1 == l2:
            continue
        else:
            return ord(l1) > ord(l2)
    return len(a) > len(b) if not a == b else False


def my_sorted2(words):
    arr = words.copy()
    for index, value in enumerate(arr[1:]):
        for j, val in enumerate(arr[index:]):
            if compare_str(arr[index + j - 1], arr[index + j]):
                local = arr[index + j]
                arr[j + index] = arr[j + index - 1]
                arr[j + index - 1] = local
    return arr

def my_sorted(words):
    arr = words.copy()
    for _ in range(2):
        arr = my_sorted2(arr)
    return arr


print(','.join(my_sorted(input().split(','))).strip(','))
'''
##same as this line from the previous git push of the daily challenge:
#print(','.join(sorted(input().split(','))).strip(','))
##but with an implementation of the sorted function.
'''
