num = int(input())
spacing = '\t'
print(spacing, end = '')
for j in range(num + 1):
    print(j, end = spacing)
print()
for i in range(num + 1):
    print(i, end = spacing)
    for j in range(num + 1):
        print(i*j, end=spacing)
    print()



