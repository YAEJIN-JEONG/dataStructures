import copy,random,time
from numpy import sort

def bubble_sort(A) :
    n = len(A)
    for i in range(n - 1):
        for j in range(n-1,i,-1):
            if (A[j - 1] > A[j]):
                A[j - 1], A[j] = A[j], A[j - 1]
        printStep(A, i+1);

def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i;
        for j in range(i+1, n) :
            if (A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i + 1);
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)
def printStep(arr, val) :
    print("Pass %2d = " % val, end='')
    print(arr)

data = [24, 15, 29, 11, 47, 12]
d = copy.deepcopy(data)
d1 = copy.deepcopy(data)
print("Before sorting ")
print(data)
print()
print("After bubble sorting ")
bubble_sort(data)
print()
print("Before sorting ")
print(d)
print()
print("After selection sorting ")
selection_sort(d)
print()
print("Before sorting ")
print(d1)
print()
print("After insertion sorting ")
insertion_sort(d1)