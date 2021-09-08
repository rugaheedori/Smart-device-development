import numpy as np

n = int(input("숫자를 입력해주세요(n <= 30) : "))
p = int(input("숫자를 입력해주세요(p <= 30) : "))

A = np.arange(1, n + 1)
B = np.arange(1, p + 1)
C = np.arange(1, max(n, p) + 1)

if (n > 30 or p > 30) :
    exit("입력 범위를 초과하였습니다.")

for i in range(min(n, p)):
    print(i)
    C[i] = A[i] + B[i]

print("A : ", A , "/", "B : ", B)  
print("C : ", C)
