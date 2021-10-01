num = int(input())
num_list = [input() for i in range(num)]
check_list = {}

result = 0

for i in num_list:
    check_list = {key: 0 for key in i}
    for index, value in enumerate(i):
        if index != len(i) - 1 and i[index] == i[index+1]:
            continue
        else:
            check_list[value] += 1
    check_num = 0
    for i in check_list.values():
        if i != 1:
            break
        check_num += 1
    if check_num == len(check_list):
        result += 1
    check_list = {}
print(result)
