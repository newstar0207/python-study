# num1 = int(input())
# num2 = int(input())

# result1 = num1 * (num2 % 10)
# result2 = num1 * (num2 % 100 // 10)
# result3 = num1 * (num2 // 100)
# print(result1)
# print(result2)
# print(result3)
# print(result1 + result2 * 10 + result3 * 100)

# num1, num2 = map(int, input().split())
# if num1 > num2:
#     print('>')
# elif num1 == num2:
#     print('==')
# else:
#     print('<')

# score = int(input())

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# num = int(input())

# if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#     print(1)
# else:
#     print(0)

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y > 0:
#     print(2)
# else:
#     print(3)

# num1, num2 = map(int, input().split())

# if num2 >= 45:
#     print(num1, num2 - 45)
# elif num2 < 45:
#     if num1 == 0:
#         print(23, num2 + 15)
#     else:
#         print(num1 - 1, num2 + 15)

# num = int(input())

# for i in range(9):
#     print(num, '*', i + 1, '=', num * (i + 1))

# num = int(input())

# for i in range(num):
#     num1, num2 = map(int, input().split())
#     print(num1 + num2)

# sum = 0
# for i in range(int(input())):
#     sum += (i + 1)
# print(sum)

# import sys
# num = int(input())
# for i in range(num):
#     num1, num2 = map(int, sys.stdin.readline().split())
#     print(num1 + num2)

# num = int(input())
# for i in range(num):
#     print(num - i)

# num = int(input())   /// 혹은 end 파라미터 를 주면 줄바꿈 안함!!!
# for i in range(num):
#     num1, num2 = map(int, input().split())
#     print('Case #%d: %d + %d =' % (i+1, num1, num2), num1+num2)

# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1) + '*' * (i + 1))


num1, num2 = map(int, input().split())
list = []
a = list(map(int, input().split()))
print(a)
# min = min(list)
# for i in range(num2):
#     print(i, end='') if i < min else print('')
