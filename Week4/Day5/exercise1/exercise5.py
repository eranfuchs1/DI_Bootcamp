find_max = lambda arr: arr[0] if len(arr) == 1 else (arr[0] if arr[0] > arr[1] else arr[1]) if len(arr) == 2 else arr[0] if arr[0] > find_max(arr[1:]) else find_max(arr[1:])

print(find_max([0,1,3,50]))
