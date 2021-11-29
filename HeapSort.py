def createheap(A):
    size=len(A)-1
    for i in reversed(range(1,size//2+1)):
        downheap(A,i,size)

def heap_sort(A) :
    n = len(A)-1
    for i in range(n):
        A[1],A[n]=A[n],A[1]
        downheap(A,1,n-1)
        n-=1
        printStep(A, i+1);
def downheap(A,i,n):
    while 2*i<n:
        k=2*i
        if k <n and A[k]<A[k+1]:
            k+=1
        if A[i]>=A[k]:
            break
        A[i],A[k] = A[k],A[i]
        i=k

def printStep(arr, val) :
    print("Pass %2d = " % val, end='')
    print(arr)

A = [-1,50, 70, 90, 30, 10, 60, 20, 40, 80]
createheap(A)
print("Before sorting ")
print(A)
print()
print("After bubble sorting ")
heap_sort(A)
print()