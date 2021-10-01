num1, num2 = input().split()
num3 = ''
num4 = ''
for i in range(3):
    num3 += num1[2 - i]
    num4 += num2[2 - i]
num3 = int(num3)
num4 = int(num4)
print(num3 if num3 > num4 else num4)
