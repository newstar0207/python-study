num = int(input())
num_list = list(map(int, input().split()))
M = max(num_list)
result_list = []
sum = 0
for x in num_list:
    result_list.append(x / M * 100)
    sum += x / M * 100
print(sum / num)
