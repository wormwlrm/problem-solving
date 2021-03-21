import sys
from collections import deque

stack = deque([])

count = int(sys.stdin.readline().rstrip())


def stack_push(value):
    stack.append(value)


def stack_pop():
    if (len(stack) == 0):
        print(-1)
    else:
        print(stack.pop())


def stack_size():
    print(len(stack))


def stack_empty():
    if (len(stack) == 0):
        print(1)
    else:
        print(0)


def stack_top():
    if (len(stack) == 0):
        print(-1)
    else:
        print(stack[-1])


for i in range(count):
    row = sys.stdin.readline().rstrip().split()
    command = row[0]

    if command == 'push':
        stack_push(row[1])
    elif command == 'pop':
        stack_pop()
    elif command == 'size':
        stack_size()
    elif command == 'empty':
        stack_empty()
    elif command == 'top':
        stack_top()
