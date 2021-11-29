import copy,random,time
from numpy import sort

def bubble_sort(A) :
    n = len(A)
    for i in range(n - 1):
        for j in range(n-1,i,-1):
            if (A[j - 1] > A[j]):
                A[j - 1], A[j] = A[j], A[j - 1]


def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i;
        for j in range(i+1, n) :
            if (A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]

def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def main():
    while True:
        n = int(input("Enter a number of data: "))
        if n == -1:
            break;
        data = []
        for i in range(n):
            numbers = random.randint(0, n)
            data.append(numbers)
        d = copy.deepcopy(data)
        d1= copy.deepcopy(data)
        d2=copy.deepcopy(data)
        startTime = time.time()
        bubble_sort(data)
        endTime = time.time()
        print("Bubble sort elapsed time: %.3f seconds" % (endTime - startTime))
        startTime = time.time()
        selection_sort(d)
        endTime=time.time()
        print("Selection sort elapsed time: %.3f seconds" % (endTime - startTime))
        startTime = time.time()
        insertion_sort(d1)
        endTime=time.time()
        print("Insertion sort elapsed time: %.3f seconds" % (endTime - startTime))
        startTime = time.time()
        sort(d2)
        endTime = time.time()
        print("Python sort elapsed time: %.3f seconds" % (endTime - startTime))

main()