import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

vertex = {}

for i in range(1, N + 1):
    vertex[i] = [i]

for i in range(M):
    to, fr = map(int, input().rstrip().split())

    vertex[fr].append(to)


max = 0

answer = []


def bfs(s):
    queue = deque()

    queue.append(s)

    # zero padding
    visited = [False] * (N + 1)

    count = 0

    while queue:
        current = queue.pop()

        if visited[current] == False:
            visited[current] = True
            count += 1
            children = vertex[current]

            for child in children:
                if visited[child] == False:
                    queue.append(child)

    return count


for i in range(1, N + 1):
    count = bfs(i)

    if count > max:
        max = count
        answer.clear()

    if count >= max:
        answer.append(i)

print(*answer)
