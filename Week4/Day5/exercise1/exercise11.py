def split_int_str(arr):
    return [arr[0] if type(arr[0]) == type(int()) else None, arr[0] if type(arr[0]) == type(str()) else None] if len(arr) == 1 else [[arr[0],] + list(filter(lambda item: item, split_int_str(arr[1:])[0])) if type(arr[0]) == type(int()) else list(filter(lambda item: item, [(split_int_str(arr[1:])[0] if type(split_int_str(arr[1:])[0]) == type(int()) else *split_int_str(arr[1:])[0])])), [arr[0],] + list(filter(lambda item: item, [(split_int_str(arr[1:])[1] if type(split_int_str(arr[1:][1])) == type(str()) else *split_int_str(arr[1:])[1])])) if type(arr[0]) == type(str()) else list(filter(lambda item: item, split_int_str(arr[1:])[1]))]

print(split_int_str(['de2 ', 233 , 43, 'rrrr',44455]))
