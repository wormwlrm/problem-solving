# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/6198%20%EC%98%A5%EC%83%81%20%EC%A0%95%EC%9B%90%20%EA%BE%B8%EB%AF%B8%EA%B8%B0

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

stack = deque([])

N = int(input())

buildings = []

answer = 0

for _ in range(N):
    buildings.append(int(input()))

for building in buildings:
    # 스택 비어있으면 그냥 넣기
    if len(stack) == 0:
        stack.append(building)
        continue

    # 제일 마지막에 있는 거보다 작을 때만 넣기
    if building < stack[-1]:
        stack.append(building)

        height = len(stack) - 1
        answer += height
        continue

    while stack and stack[-1] <= building:
        stack.pop()

    stack.append(building)

    height = len(stack) - 1
    answer += height


print(answer)
