str_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_str = input()
result = 0

while True:
    if len(input_str) == 0:
        break
    for s in str_list:
        if input_str.startswith(s):
            input_str = input_str[len(s):]
            result += 1
            break
        if s == str_list[-1]:
            input_str = input_str[1:]
            result += 1
print(result)
