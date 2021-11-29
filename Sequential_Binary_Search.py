import copy, random, time
from numpy import sort

def sequential_search(A, key):
    low = 0
    high = len(A) - 1
    for i in range(low, high + 1):
        if A[i] == key:
            return i
    return -1

def binary_search(A, key) :
    low=0
    high=len(A)-1
    while (low <= high) :
        middle = (low + high) // 2
        if A[middle]==key:
            return middle
        elif (int(key) > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
    return -1

def main():
    n = int(input("Enter a number of data: "))
    data = []
    for i in range(n):
        numbers = random.randint(0, n)
        data.append(numbers)
    d = copy.deepcopy(data)
    d1=copy.deepcopy(data)
    startTime = time.time()
    sort(data)
    endTime = time.time()
    print("Python sort elapsed time: %.3f seconds" % (endTime - startTime))
    print()
    while True:
        s=input("Enter a number to search: ")
        if s == '-1':
            break;
        startTime = time.time()
        sequential_search(d,s)
        if '-1':
            print(s+" is not in the list")
        else:
            print(s+" is in the list at index ")
        endTime = time.time()
        print("Sequential search elapsed time: %.3f seconds" % (endTime - startTime))
        startTime = time.time()
        binary_search(d1, s)
        if '-1':
            print(s+" is not in the list")
        else:
            print(s + " is in the list at index ")
        endTime = time.time()
        print("Binary search elapsed time: %.3f seconds" % (endTime - startTime))
        print()

main()
