# # 단어의 개수

# num = input().split()
# print(len(num))

# # 단어 공부

# str = input().lower()
# strList = list(str)
# setStrList = set(str)
# dic = {key: 0 for key in strList}

# for i in str:
#     dic[i] += 1

# values = list(dic.values())
# values.sort(reverse=True)

# if len(str) == 1:
#     print(str.upper())
# elif values[0] == values[1]:
#     print('?')
# else:
#     for j in setStrList:
#         if dic[j] == values[0]:
#             print(j.upper())


# # 엄청난 부자

# num1, num2 = input().split()
# num1 = int(num1)
# num2 = int(num2)
# print(num1 // num2)
# print(num1 % num2)


# # 베스트 셀러

# bookNum = int(input())
# bookList = [input() for i in range(bookNum)]

# dic = {key: 0 for key in bookList}
# for i in bookList:
#     dic[i] += 1

# dicKeys = list(dic.keys())
# dicKeys.sort()
# dicValues = list(dic.values())
# dicValues.sort(reverse=True)

# for j in dicKeys:
#     if dic[j] == dicValues[0]:
#         print(j)
#         break


# # 듣보잡

# num1, num2 = map(int, input().split())
# list1 = [input() for i in range(num1)]
# list2 = [input() for i in range(num2)]
# list1 = set(list1)
# list2 = set(list2)
# print(len(list1 & list2))

# resultList = list(list1 & list2)
# resultList.sort()
# for i in resultList:
#     print(i)

# print(1 / 3)
