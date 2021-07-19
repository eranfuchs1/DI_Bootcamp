# 1. a float is a number that has a decimal point, for example 1.2
print(dir(float))

# 2.
print([f/3 for f in range(2,41)])

# 3.
for i in range(3,10):
    num = float(i) * 0.5
    if int(num) == num:
        print(int(num), end = ' ')
    else:
        print(num, end = ' ')
print()
