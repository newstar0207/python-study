num_dic = {key: '' for key in range(10)}
ascii_num = 65

for i in range(10):
    if i == 1 or i == 0:
        num_dic[i] = ''
    elif i == 7 or i == 9:
        for x in range(4):
            num_dic[i] += chr(ascii_num)
            ascii_num += 1
    else:
        for x in range(3):
            num_dic[i] += chr(ascii_num)
            ascii_num += 1

input_str = input()
sum = 0

for i in input_str:
    for key in num_dic.keys():
        for value in num_dic[key]:
            if i == value:
                sum += key + 1
                break

print(sum)
