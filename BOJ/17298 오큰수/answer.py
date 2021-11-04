# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/17298%20%EC%98%A4%ED%81%B0%EC%88%98

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

numbers = list(map(int, input().split()))

stack = deque([])

answer = [-1] * (N)

for index, number in enumerate(numbers):
    if len(stack) == 0:
        stack.append((index, number))
        continue

    while len(stack) > 0:
        last_index, last_value = last = stack[-1]

        if last_value < number:
            answer[last_index] = number
            stack.pop()
        else:
            break

    stack.append((index, number))

print(*answer)
