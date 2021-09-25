x = int(input())
y = int(input())
z = int(input())
mul = x * y * z
mul_list = list(str(mul))
num_dic = {key: 0 for key in range(10)}
for x in mul_list:
    num_dic[int(x)] += 1

for x in num_dic:
    print(num_dic[x])
