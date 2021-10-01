stack = []
size = len(stack)
top = -1


def push(data):
    global top
    if top < size - 2:
        stack[top] = data
        top += 1
    else:
        print('stack overflow')


def pop():
    # print(stack[top])
    stack[top - 1] = 0


push(3)
pop()
push(2)
push(3)
pop()


print(num_list)
