import numpy as np

mat = []
plus = []

inp = input()

m = str(inp).split(' ')[0]
n = str(inp).split(' ')[1]

for c in range(int(m)):
    mat.append([int(i) for i in input().split(' ')[:int(n)]])

for c in range(int(m)):

    plus.append([int(i) for i in input().split(' ')[:int(n)]])

[print(" ".join(map(str,i))) for i in np.array(mat) + np.array(plus)]
