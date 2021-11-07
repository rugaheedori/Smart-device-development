import numpy as np
import threading

B = np.zeros((10,10))
print("Array B :\n", B)

def change_area(num1, num2, num3):
    if (num1 == 5):
        start1 = 0
        end1 = num1
    else:
        start1 = 5
        end1 = num1
    
    if (num2 == 5):
        start2 = 0
        end2 = num2
    else:
        start2 = 5
        end2 = num2

    for i in range(start1, end1) :
        for j in range(start2, end2):
            B[i, j] = num3

t1 = threading.Thread(target=change_area, daemon=False, args=(5, 5, 7))
t1.start()
t2 = threading.Thread(target=change_area, daemon=False, args=(5, 10, 87))
t2.start()
t3 = threading.Thread(target=change_area, daemon=False, args=(10, 5, 19))
t3.start()
t4 = threading.Thread(target=change_area, daemon=False, args=(10, 10, 6))
t4.start()

print("Array B :\n", B)