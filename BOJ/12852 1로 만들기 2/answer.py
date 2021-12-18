# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/12852%201%EB%A1%9C%20%EB%A7%8C%EB%93%A4%EA%B8%B0%202

import sys
from collections import deque


input = lambda: sys.stdin.readline().rstrip()

visited = {}

prev = {}

N = int(input())

queue = deque([N])

turn = -1

prev[N] = -1
visited[N] = -1


def print_traversal():
    start = 1
    answer = []

    while start != -1:
        answer.append(start)
        start = prev[start]

    print(*reversed(answer))


while queue:
    turn += 1

    for _ in range(len(queue)):
        current = queue.popleft()

        if current == 1:
            print(turn)
            print_traversal()
            exit(0)

        # 3의 배수일 때
        if current % 3 == 0:
            divided = current // 3

            if divided not in visited or visited[divided] > turn:
                visited[divided] = turn
                prev[divided] = current

                queue.append(divided)

        # 2의 배수일 때
        if current % 2 == 0:
            divided = current // 2

            if divided not in visited or visited[divided] > turn:
                visited[divided] = turn
                prev[divided] = current

                queue.append(divided)

        # 1 뺄 때
        subtracted = current - 1

        if (subtracted not in visited or visited[subtracted] > turn) and subtracted > 0:
            prev[subtracted] = current
            visited[subtracted] = turn
            queue.append(subtracted)
