front = 0
rear = -1
queue = []


def put(data):
    global front
    global rear
    queue.append(data)
    # front += 1
    rear += 1


def get():
    global front
    global rear
    queue[front]
    front -= 1
    del queue[front]
