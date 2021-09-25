num = [input() for x in range(10)]
num_set = set()
for x in num:
    num_set.add(int(x) % 42)
print(len(num_set))
