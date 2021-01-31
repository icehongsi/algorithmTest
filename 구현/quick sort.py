import random
import sys
sys.setrecursionlimit(1<<15)

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    A, M, B = [], [pivot], []
    for i in range(len(array) - 1):
        if array[i] < pivot:
            A.append(array[i])
        elif array[i] > pivot:
            B.append(array[i])
        else:
            M.append(array[i])


    return quicksort(A) + M + quicksort(B)

for i in range(10):
    test = []
    for j in range(100):
        test.append(random.randint(1, 1000))
    print(quicksort(test))