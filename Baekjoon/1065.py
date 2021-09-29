def a(num):
    result = 0
    for i in range(num):
        num_list = list(map(int, str(i + 1)))
        if len(num_list) == 1:
            result += 1
            continue
        else:
            d = num_list[1] - num_list[0]
            x = 0
            for j in range(len(num_list) - 1):
                x += num_list[j+1] - num_list[j]
                if d * (len(num_list) - 1) == x and j == len(num_list) - 2:
                    result += 1
    return print(result)


a(int(input()))
