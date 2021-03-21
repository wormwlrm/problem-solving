import sys
from collections import deque

queue = deque([])

count = int(sys.stdin.readline().rstrip())


def queue_push(value):
    queue.append(value)


def queue_pop():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue.popleft())


def queue_size():
    print(len(queue))


def queue_empty():
    if (len(queue) == 0):
        print(1)
    else:
        print(0)


def queue_front():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[0])


def queue_back():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[-1])


for i in range(count):
    row = sys.stdin.readline().rstrip().split()
    command = row[0]

    if command == 'push':
        queue_push(row[1])
    elif command == 'pop':
        queue_pop()
    elif command == 'size':
        queue_size()
    elif command == 'empty':
        queue_empty()
    elif command == 'front':
        queue_front()
    elif command == 'back':
        queue_back()
