num1, num2, num3 = map(int, input().split())
i = 1

while True:
    if num2 >= num3:
        print(-1)
        break
    else:
        print(num1 // (num3 - num2) + 1)
        break
    i += 1
