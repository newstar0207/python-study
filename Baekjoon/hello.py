# name = 'hello'
# age = 20
# score = 4.3

# int_value1, int_value2 = 10, 20

# print('hello')
# print('hello' + name)
# print('hello' , name)
# print(name, age)

# str = input()
# age = int(input())
# score = float(input())
# print(str, age, score)

# first_name, last_name = input().split()
# print(first_name, last_name)

# year, month = map(int, input().split())
# print(year, month)

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# A, B, C = map(int, input().split())
# print('\    /\\')
# print(" )  ( ')")
# print('(  /  )')
# print(' \(__)|')

# list = []
# list2 = [1, 2, 3, True, False]
# list3 = [(1, 2, 3), {'name': 'user'}, [1, 2, 3]]
# list4 = [list, list3]
# print(list, list2)
# print(list3)
# print(len(list4), list4)

# list = [1, 2, 3, 4, 5]
# print(list[2], list[3])

# list = [0, 1, 2, 3, 4, 5]
# print(list.index(2))
# list.insert(3, -1)
# print(list)
# list.append(6)
# list.extend([7, 8])
# print(list)
# list.sort()
# print('sort', list)
# list.sort(reverse=True)
# print('reverse sort', list)
# list.reverse()
# print('reverse', list)

# list = [1, 2, 3, 4, 5]
# list.insert(0, 6)
# list.append(0)
# print(list)
# list.sort()
# print(list)


# list = [1, 2, 3, 4, 5]
# del list[1]
# print(list, len(list))
# list.remove(1)
# print(list, len(list))

# list = [1, 2, 3, 4, 5]
# delNum = int(input())
# list.remove(delNum)
# print(list)

# list = [0, 1, 2, 3, 4, 5, 6, 7]
# print(list[len(list) - 1])
# print(list[-5])

first = 'hello "you"'
second = "hello 'you'"
multi1 = '''hello 
friend'''
multi2 = """hello
friend"""

# print(first, second)
# print(first[0], second[-1])
# print(multi1)
# print(multi2)

# str = 'hello my friend'
# split_default = str.split()
# split_char = str.split('e')
# print(split_default)
# print(split_char)

# str_list = list(str)
# print(str_list)

# joined_empty = ''.join(str_list)
# joined_char = '-'.join(str_list)

# print(joined_empty)
# print(joined_char)

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sub1 = list[5:8]
# sub2 = list[7:]
# sub3 = list[:4]
# sub4 = list[::2]
# print(sub1)
# print(sub2)
# print(sub3)
# print(sub4)
# print(list[::-1])
# print(list[8:3:-1])
# print(list[-2:-4:-1])

# print(list)
# del list[:3]
# print(list)
# del list[2:5]
# print(list)

# str = input()
# print(str[:3] + str[-3:])

# capitals = {'korea': 'seoul', 'uk': 'london'}
# print(capitals['korea'])
# capitals['japan'] = 'tokyo'
# print(capitals)

# capitals.update({'usa': 'washington', 'china': 'beijing'})
# print(capitals)
# del capitals['usa']
# print(capitals)

# set1 = set([1, 2, 3, 4])
# set2 = {(1, 2), 2, 3, 'hello'}
# print(set1)
# print(set2)
# set1.add(5)
# print(set1)
# set1.add(1)
# print(set1)
# set1.remove(4)
# print(set1)
# set1.update([6, 7])
# print(set1)
# # set1.add({'1': '2'})

# print(set1 & set2)
# print(set1 | set2)
# print(set1 - set2)

# num = int(input())

# if num >= 0:
#     print('ok')
# elif num <= -1:
#     print('ng')

# str = input()

# if len(str) > 7:
#     print('ok')
# else:
#     print('NG')

# num1, num2 = map(int, input().split())

# if num1 > 0 and num2 > 0:
#     print('ok')
# else:
#     print('NG')

# num = int(input())

# if num == 0:
#     print('0')
# elif num % 2 == 0:
#     print('even')
# else:
#     print('odd')

# age = 18

# if age > 19:
#     print('adult')
# elif 19 >= age > 12:
#     print('teenager')
# else:
#     print('kid')

# str = len(input())

# if 10 >= str >= 4:
#     print('ok')
# else:
#     print('ng')

# age = int(input())

# print('hello' if age > 19 else 'hi')

# num1, num2 = map(int, input().split())

# print('OK' if (num1 + num2) >= 0 else 'NG')

# num1, num2 = map(int, input().split())
# operator = input()
# print(num1 + num2) if operator == '+' else print(num1 - num2)

# arr = [1, 3, 5, 7]

# for a in arr:
#     print(a)

# for b in [2, 4, 6, 8]:
#     print(b)

# for c in arr[::2]:
#     print(c)

# tp = (1, 2, 3, 4, 5)

# for t in tp:
#     print(t)

# str = 'hello world!'

# for s in str:
#     print(s)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for l in list[1::2]:
#     print(l)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# evenArr = 0
# oddArr = 0

# for n in arr:
#     if n % 2 == 0:
#         evenArr += n
#     else:
#         oddArr += n

# print(evenArr)
# print(oddArr)


# for i in range(5):
#     print(i)

# for i in range(5, 10):
#     print(i)
# for i in range(1, 10, 2):
#     print(i)


# for i in range(2, 10):
#     print('2 *', i, '=', 2 * i)

# for i in range(1, 5):
#     for j in range(0, i):
#         print('*', end='')  # 줄바꿈 안됨
#     print()

# arr = [10, 11, 12, 13]

# for i, v in enumerate(arr):
#     print(i, v)

# arr = ['a', 'b', 'c']

# for i, v in enumerate(arr):
#     print(i, v)

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|


# arr1 = [10, 11, 12, 13]
# arr2 = [1, 2, 3, 4, ]
# arr3 = ['hello', 'world', '!', '!']

# for i, j, k in zip(arr1, arr2, arr3):
#     print(i, j, k)

# arr = [i for i in range(5, 10)]
# print(arr)

# arr2 = [i * 2 for i in range(3)]
# print(arr2)

# arr3 = [[i, j] for i in range(3) for j in range(10, 13)]
# print(arr3)

# arr3 = [0] * 10
# print(arr3)

# arr = [i for i in range(1, 11, 2)]

# n = int(input())
# arr = [input() for i in range(n)] # return 되는 i 를 쓰지 않고 input()으로만 넣을것이다

# arr = [i for i in range(10) if i % 2 == 0]
# print(arr)

# scores = [80, 95, 66, 88, 90, 70, 74, 98]
# a_grade = [s for s in scores if s >= 90]
# print(a_grade)

# n = int(input())

# arr1 = [int(input()) for i in range(n)]
# arr2 = [n for n in arr1 if n >= 0]
# for i in arr2:
#     print(i)

# set1 = set([2, 3, 3, 3])
# print(set1)
