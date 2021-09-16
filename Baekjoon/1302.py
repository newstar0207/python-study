bookNum = int(input())
bookList = [input() for i in range(bookNum)]

dic = {key: 0 for key in bookList}
for i in bookList:
    dic[i] += 1

dicKeys = list(dic.keys())
dicKeys.sort()
dicValues = list(dic.values())
dicValues.sort(reverse=True)

for j in dicKeys:
    if dic[j] == dicValues[0]:
        print(j)
        break
