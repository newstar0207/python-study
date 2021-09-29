def d(num):
    nums_bool = [False for i in range(num + 1)]
    for i in range(num + 1):
        for x in str(i):
            i += int(x)
        if i > num:
            continue
        nums_bool[i] = True
    for i, v in enumerate(nums_bool):
        if v == False:
            print(i)


d(10000)
