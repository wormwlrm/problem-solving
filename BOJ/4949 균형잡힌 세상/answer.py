from collections import deque 
import sys

input = sys.stdin.readline

while True:
    line = str(input().rstrip())

    if (line == '.'):
        break

    stack = deque([])

    is_balanced = True

    for i in list(line):
        if (i == '(') or (i == '['):
            stack.append(i)

        if (i == ')'):
            if (len(stack) == 0):
                is_balanced = False
                break

            pair = stack.pop()
            if (pair != '('):
                is_balanced = False
                break

        if (i == ']'):
            if (len(stack) == 0):
                is_balanced = False
                break

            pair = stack.pop()
            if (pair != '['):
                is_balanced = False
                break

    # 짝 맞춘 후 남아있으면 안됨
    if (len(stack) > 0):
        is_balanced = False

    print('yes') if is_balanced else print('no')
