import numpy as np

A = np.arange(1, 21)

for i in range (20) :
   if (i < 10) : 
       A[i] = 2 * i + 1
   else: 
       A[i] = (i - 9) * 2

print(A)