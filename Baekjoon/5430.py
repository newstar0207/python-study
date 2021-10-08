def reverse_f():
    global index
    index += 1
    index *= -1
    return index


def delete_f(input_list):
    global index
    if len(input_list) == 0:
        return 'error'
    del input_list[index]
    return input_list


# sys.stdin.readline().rstrip()
test_case_num = int(input())
result = []
index = 0

for i in range(test_case_num):
    p_list = list(input())
    n = int(input())
    num_str = input()
    index = 0
    if n >= 1:
        num_list = list(map(int, num_str[1: -1].split(',')))
    else:
        num_list = []
    for p in p_list:
        if p == 'R':
            index = reverse_f()
        else:
            num_list = delete_f(num_list)
            if num_list == 'error':
                break
    if index == -1 and num_list != 'error':
        num_list.reverse()
        result.append(num_list)
    else:
        result.append(num_list)

for i in result:
    if i == 'error':
        print('error')
    else:
        i = str(i)
        i = i.replace(' ', '')
        print(i)
