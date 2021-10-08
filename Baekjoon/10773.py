import sys

num = int(sys.stdin.readline().rstrip())
sum = 0
stack = []

for i in range(num):
    add_num = int(sys.stdin.readline().rstrip())
    if add_num == 0:
        sum -= stack[-1]
        stack.pop()
    else:
        stack.append(add_num)
        sum += add_num
print(sum)
