# 리스트 lst = [7, 2, 6, 4, 5]와 같이 리스트를 선언하고
# 리스트의 모든 값을 더해 결과를 반환하는 함수를 구현한 후 함수 호출하여 결과를 출력한다.
list = [7, 2, 6, 4, 5]
def sumList(list):
    sum=0
    for i in list :
        sum+=i
    return sum
print("list : ",list)
print("Sum of list : ",sumList(list))