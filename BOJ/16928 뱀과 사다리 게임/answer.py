import sys
from collections import deque

input = sys.stdin.readline

ladder_count, snake_count = map(int, input().split())

ladder_and_snake = {i: i for i in range(1, 101)}

for _ in range(ladder_count):
    x, y = map(int, input().split())
    ladder_and_snake[x] = y

for _ in range(snake_count):
    u, v = map(int, input().split())
    ladder_and_snake[u] = v


def get_children(position):
    children = []

    for i in range(1, 7):
        if 1 <= position + i <= 100:
            children.append(ladder_and_snake[position + i])

    return children


depth = 0

queue = deque([1, None])

answer = 0

distance = [0] + [float("inf")] * 100

while queue:
    current = queue.popleft()

    if current == None:
        if len(queue) == 0:
            break

        queue.append(None)
        depth += 1
        continue

    if depth > distance[current]:
        continue

    distance[current] = depth

    if current == 100:
        break

    children = get_children(current)

    for child in children:
        queue.append(child)

print(distance[100])
