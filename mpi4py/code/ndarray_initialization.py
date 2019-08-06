

import numpy as np
import random


#mat = np.arange().reshape(6,4)
#mat = np.empty(24, dtype=np.int64).reshape(6,4)
mat = np.zeros((6,4), dtype='i')

print(mat)
for i in range(0,6):
    for j in range(0,4):
        print(mat[i][j])

for i in range(0,6):
    for j in range(0,4):
        mat[i][j] = random.randint(0, 20)

print(mat)
