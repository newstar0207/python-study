str = input().upper()
strList = list(str)
setStrList = set(str)
dic = {key: 0 for key in strList}

print(dic)

for i in str:
    dic[i] += 1

values = list(dic.values())
values.sort(reverse=True)

if len(str) == 1:
    print(str)
elif values[0] == values[1]:
    print('?')
else:
    for j in setStrList:
        if dic[j] == values[0]:
            print(j)
