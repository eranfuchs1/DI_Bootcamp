list_count = lambda arr, item: (1 if arr[0] == item else 0) + list_count(arr[1:], item) if len(arr) > 0 else 0

print(list_count(['a','a','t','o'],'a'))
