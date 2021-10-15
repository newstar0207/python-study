min, max = map(int, input().split())
result = [x for x in range(min, max + 1)]

for i in range(2, int((max + 1) ** (1/2)) + 1):
    for j in range(i + i, max + 1, i):
        if j < min:
            continue
        result[j - min] = 0

for i in result:
    if i != 0 and i != 1:
        print(i)
