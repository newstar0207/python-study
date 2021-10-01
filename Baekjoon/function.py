def say_hello(name):
    print('hello', name)


def say_bye(name):
    print('bye', name)


def add(first, second):
    print(first, '+', second, '=', first+second)


def bigger(first, second):
    print(first) if first >= second else print(second)


def hello(age, name='user'):  # default 값이 있는 파라미터는 가장 뒤에 둠
    print('hello', name, age)


def print_tp(*t):
    print(t)


def print_dic(**d):
    print(d)


def sum_int(*t):
    sum = 0
    for t in t:
        if type(t) == int:
            sum += t
    print(sum)


def param1(a, b, c=5, *t):
    print(c)
    print(t)


def param2(a, *t, b, c=3):
    print(c)
    print(t)


def param3(*t, a, b, c=3):
    print(c)
    print(t)


def func(first, second):
    print(first, second)


def add(first, second):
    return first+second


def int_func():
    return 1


def float_func():
    return 1.1


def list_func():
    return [1, 2, 3]


def set_func():
    return {1, 2, 3}


def tuple_func():
    return 1, 2, 3


def dic_func():
    return {1: 1, 2: 2, 3: 3}


def min_int(*t):
    # list_int = list(t)
    return min(t)


def func():
    return 1, 2, 3


def info(list_int):
    sum = 0
    for x in list_int:
        sum += x
    return sum, sum / len(list_int)


def min_max(list_int):
    max = list_int[0]
    min = list_int[0]
    for x in list_int:
        if x >= max:
            max = x
        if x <= min:
            min = x
    return min, max

# 지역변수, 전역 변수
# sum = 0


def total(values):
    sum = 0
    for i in values:
        sum += i
    print(sum)


def total(values):
    global sum
    for i in values:
        sum += i
    print(sum)


# Call by object reference
def func(first, second):
    first += 10
    second.add(4)


def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)


def rc_factorial1(n):
    fac = 1
    for x in range(n):
        fac *= x + 1
    return fac


def rc_factorial2(n):
    # fac *= n
    # print(fac)
    # if(n-1 == 1):
    #     return fac
    # return rc_factorial2(n-1, fac)
    if n < 2:
        return 1
    return n * rc_factorial2(n-1)


# def my_range(*num) :
#     if len(num) == 1 :
#         start = 0
#         end = num[0]
#     elif len(num) == 2 :


# 고차함수

def add(first, second):
    return first + second


def sub(first, second):
    return first - second


def executor(func, op, param1, param2):
    return func[op](param1, param2)

# func = {'+': add, '-': sub}
# print(executor(func, '+', 1, 2))
# print(executor(func, '-', 1, 2))


def calculate(op, num1, num2):  # 외부에서 내부함수를 호출 못함
    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    if op == '+':
        return add(num1, num2)
    else:
        return sub(num1, num2)


# print(calculate('+', 1, 2))

# selection = int(input())
# if selection == 1:
#     def func():
#         print('hello')
# else:
#     def func():
#         print('bye')


# 예외처리

# num = 0
# try:
#     num = int(input())
# except ValueError:
#     num = 0
# finally:
#     print(num)

# list = [1,2,3]
# value = 0
# try :
#     index = int(input())
#     valu


# print(rc_factorial2(5))

# count_down(5)

# number = 1  # immutalbe
# set = {1, 2, 3}  # mutable
# func(number, set)
# print(number, set)

# total([1, 2, 3])
# print(sum)


# min, max = min_max([10, 2, 3, 4, 5, 6, 7, 8, 9, 1])
# print(min, max)

# sum, avg = info([1, 2, 3, 4, 5])
# print(sum, avg)

# tp = func()
# print(type(tp))

# x, y, z = func()
# x = 1000
# print(x, y, z)


# print(min_int(1, 2, 3, 4, 5, -3))


# print(int_func(), type(int_func()))
# print(float_func(), type(float_func()))
# print(list_func(), type(list_func()))
# print(set_func(), type(set_func()))
# print(tuple_func(), type(tuple_func()))
# print(dic_func(), type(dic_func()))
# print(add(1, 2))


# param1 = [1, 2]
# param2 = (3, 4)
# func(*param1)
# func(*param2)
# func(*[5, 6])
# dic = {'first': 1, 'second': 2}
# func(**dic)

# param1(1, 2, 3, 4)
# param2(1, 2, 3, b=4)
# param3(1, 2, a=3, b=4, c=5)

# sum_int(1, 2323, 1.0, '1', False)

# print_tp(1, 2, 3, 4, 5)
# print_dic(first=1, second=2)

# hello(20)
# hello(20, 'abc')
# bigger(3, 30)


# add(1, 2)
# add(second=8, first=10)

# say_hello('saybyul')
# say_bye('saybyul')
