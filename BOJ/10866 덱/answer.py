import sys
from collections import deque

deq = deque([])

count = int(sys.stdin.readline().rstrip())


def deq_push_front(value):
    deq.appendleft(value)


def deq_push_back(value):
    deq.append(value)


def deq_pop_front():
    if (len(deq) == 0):
        print(-1)
    else:
        print(deq.popleft())


def deq_pop_back():
    if (len(deq) == 0):
        print(-1)
    else:
        print(deq.pop())


def deq_size():
    print(len(deq))


def deq_empty():
    if (len(deq) == 0):
        print(1)
    else:
        print(0)


def deq_front():
    if (len(deq) == 0):
        print(-1)
    else:
        print(deq[0])


def deq_back():
    if (len(deq) == 0):
        print(-1)
    else:
        print(deq[-1])


for i in range(count):
    row = sys.stdin.readline().rstrip().split()
    command = row[0]

    if command == 'push_back':
        deq_push_back(row[1])
    elif command == 'push_front':
        deq_push_front(row[1])
    elif command == 'pop_front':
        deq_pop_front()
    elif command == 'pop_back':
        deq_pop_back()
    elif command == 'size':
        deq_size()
    elif command == 'empty':
        deq_empty()
    elif command == 'front':
        deq_front()
    elif command == 'back':
        deq_back()
