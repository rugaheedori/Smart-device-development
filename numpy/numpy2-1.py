import numpy as np

A = np.arange(1, 21)

for i in range (5) :
    B = A[i]
    A[i] = A[9 - i]
    A[9 - i] = B

print(A)