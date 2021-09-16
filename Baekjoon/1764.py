num1, num2 = map(int, input().split())
list1 = [input() for i in range(num1)]
list2 = [input() for i in range(num2)]
list1 = set(list1)
list2 = set(list2)
print(len(list1 & list2))

resultList = list(list1 & list2)
resultList.sort()
for i in resultList:
    print(i)
