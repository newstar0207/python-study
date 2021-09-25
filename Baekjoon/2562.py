nums = [[int(input()), x+1] for x in range(9)]
max = nums[0][0]
index = 0
for x in range(9):
    if max <= nums[x][0]:
        max = nums[x][0]
        index = nums[x][1]
print(max)
print(index)
