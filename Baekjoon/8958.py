num = int(input())
list = [input() for x in range(num)]
result = 0
result_list = []
sum = 1
for x in list:
    sum = 1
    result = 0
    for i in x:
        if(i == 'X'):
            sum = 1
        if(i == 'O'):
            result += sum
            sum += 1
    print(result)
