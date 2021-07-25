def is_mono(arr):
    return ((arr[-1] > arr[-2] and is_mono(arr[:-1]) == -1) or (arr[-1] <= arr[-2])) if len(arr) > 2 else -1 if arr[-1] > arr[-2] else 1

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))
