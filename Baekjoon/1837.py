p_num, k_num = map(int, input().split())
result = [x for x in range(1, k_num + 1)]
result[0] = 0

for i in range(2, int(k_num ** (1/2) + 1)):
    for j in range(i + i, k_num+1, i):
        result[j - 1] = 0

# print(result)

for i, num in enumerate(result):
    if num == 0 and i != len(result) - 1:
        continue
    if i == len(result) - 1:
        print('GOOD')
        break
    if p_num % num == 0 and num != k_num:
        print('BAD', num)
        break
