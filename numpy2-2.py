import numpy as np

A = np.arange(1, 21)

for i in range (10) :
    B = A[i]
    A[i] = A[10 + i]
    A[10 + i] = B

print(A)