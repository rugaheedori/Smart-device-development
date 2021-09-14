import numpy as np

n = int(input("숫자를 입력해주세요(n <= 30) : "))
p = int(input("숫자를 입력해주세요(p <= 30) : "))

if (n > 30 or p > 30) :
    exit("입력 범위를 초과하였습니다.")

A = np.arange(1, n + 1)
A[p] = A[n - p - 1]
print("A :", A)