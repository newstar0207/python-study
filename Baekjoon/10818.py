num = int(input())
nums = list(map(int, input().split()))
min = nums[0]
max = nums[0]

for x in nums:
    if x > max:
        max = x
    if x < min:
        min = x

print(min, max)
