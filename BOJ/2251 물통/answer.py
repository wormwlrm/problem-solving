import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

visited = {}

answer = []

queue = deque([(0, 0, C)])

maximum = {0: A, 1: B, 2: C}


def movable(status, start, end):
    if status[start] <= 0:
        return False

    if status[end] >= maximum[end]:
        return False

    return True


def move(status, start, end):
    movable_amount = min(status[start], maximum[end] - status[end])

    if start == 0:
        if end == 1:
            answer = (status[0] - movable_amount, status[1] + movable_amount, status[2])
        elif end == 2:
            answer = (status[0] - movable_amount, status[1], status[2] + movable_amount)
    elif start == 1:
        if end == 0:
            answer = (status[0] + movable_amount, status[1] - movable_amount, status[2])
        elif end == 2:
            answer = (status[0], status[1] - movable_amount, status[2] + movable_amount)
    elif start == 2:
        if end == 0:
            answer = (status[0] + movable_amount, status[1], status[2] - movable_amount)
        elif end == 1:
            answer = (status[0], status[1] + movable_amount, status[2] - movable_amount)

    return answer


while queue:
    current = queue.popleft()

    visited[current] = True

    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            if movable(current, i, j):
                moved = move(current, i, j)
                if moved not in visited:
                    queue.append(moved)


answer = set([])
for key in visited.keys():
    if key[0] == 0:
        answer.add(key[2])


print(*sorted(answer))
