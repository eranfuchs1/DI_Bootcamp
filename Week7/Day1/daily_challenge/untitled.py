from random import randint


N = randint(1,40)
M = randint(1,50)

table = [[randint(1,100) for j in range(N)] for i in range(M)]

print(table[2])

print([i[2] for i in table])


table[-1] = [7 for j in range(N)]

print(table)


for i, ival in enumerate(table):
    table[i][-1] = ival[0] + ival[1]
print(table)

import numpy as np

table = np.array([randint(1,100) for _ in range(M*N)]).reshape((N,M))

print(table[2])
print(table[:,2])

table[-1] = 7
print(table)

table[:,-1] = table[:,0] + table[:,1]

print(table)
