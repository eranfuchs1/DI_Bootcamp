print_longest = lambda arr: print_longest(arr[1:]) if len(arr[0]) < max([len(word) for word in arr]) else print(arr[0])

print_longest(['aa', 'aaaaaaa', 'eqv'])
