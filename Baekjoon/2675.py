str_list = []
for i in range(int(input())):
    str_list.append(list(input().split()))

for i in str_list:
    for j in i[1]:
        for k in range(int(i[0])):
            print(j, end='')
    print()
