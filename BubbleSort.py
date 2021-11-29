def bubble_sort(A) :
    n = len(A)
    for i in range(n - 1):
        for j in range(n-1,i,-1):
            if (A[j - 1] > A[j]):
                A[j - 1], A[j] = A[j], A[j - 1]
        printStep(A, i+1);

def printStep(arr, val) :
    print("Pass %2d = " % val, end='')
    print(arr)

A = [30, 60, 90, 10, 40, 80, 40, 20, 10, 60, 50, 30, 40, 90, 80]
print("Before sorting ")
print(A)
print()
print("After bubble sorting ")
bubble_sort(A)
print()