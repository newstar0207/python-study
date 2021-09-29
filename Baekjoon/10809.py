result = [-1] * 26

for i, v in enumerate(input()):
    if result[ord(v) - 97] == -1:
        result[ord(v) - 97] = i

for i in result:
    print(i, end=' ')
