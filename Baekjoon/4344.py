num = int(input())
num_list = [list(map(int, input().split())) for x in range(num)]
sum = 0
avg = 0
result = 0
for num in num_list:
    sum = 0
    avg = 0
    result = 0
    for i in range(len(num) - 1):
        sum += num[i + 1]
    avg = sum / num[0]
    for i in range(len(num) - 1):
        if num[i + 1] > avg:
            result += 1
    result = result / num[0] * 100
    print('{:.3f}%'.format(round(result, 3)))
