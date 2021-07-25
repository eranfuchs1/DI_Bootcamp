from math import sqrt
norm = lambda arr: int(sqrt(sum(map(lambda num: num * num, arr))))

print(norm([1,1,2]))
