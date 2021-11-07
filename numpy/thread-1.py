import numpy as np
import threading

A = np.zeros(20)
print("Array A :", A)

def forward():
    for i in range(10):
        A[i] = i
        
def backward():
    for i in range(10, 20):
        A[i] = 19 - i

t1 = threading.Thread(target=forward, daemon=False, args=())
t1.start()
t2 = threading.Thread(target=backward, daemon=False, args=())
t2.start()

print("Array A :", A)


 
