num = int(input())
num_list = [int(input()) for x in range(num)]
large_num = max(num_list)
fibonacci = {0: [1, 0], 1: [0, 1]}


for i in range(large_num - 1):

    fibonacci[i + 2] = [fibonacci[i + 1][0] + fibonacci[i]
                        [0], fibonacci[i + 1][1] + fibonacci[i][1]]


for i in num_list:
    print(fibonacci[i][0], fibonacci[i][1])
