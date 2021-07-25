my_sum = lambda arr: arr[0] + my_sum(arr[1:]) if len(arr) > 1 else arr[0]

print(my_sum([1,5,4,2]))
