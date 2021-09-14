import numpy as np

n = int(input("숫자를 입력해주세요(n <= 10) : "))
p = int(input("숫자를 입력해주세요(p <= 10) : "))

if (n > 10 or p > 10) :
    exit("입력 범위를 초과하였습니다.")

A = np.arange(1, 50, n)
B = np.arange(1, 50, p)
C = np.intersect1d(A, B)

print("A : ", A , "/", "B : ", B)
print("C : ", C)