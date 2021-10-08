stack = []
result = []

while True:
    input_str = input()
    stack = []
    if input_str == '.':
        break
    for k in input_str:
        if k == '(' or k == '[':
            stack.append(k)
        if k == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack = 'error'
                break
        if k == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack = 'error'
                break
    if len(stack) != 0:
        print('no')
    elif stack == 'error':
        print('no')
    else:
        print('yes')
