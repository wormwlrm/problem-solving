import sys
from math import isinf
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# zero padding
cost = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())

    cost[u][v] = 1
    cost[v][u] = 1

visited = [False] * (N + 1)

answer = 0

for i in range(1, N + 1):
    if visited[i] == True:
        continue

    queue = deque([i])
    visited[i] = True

    while queue:
        current = queue.popleft()

        for index, value in enumerate(cost[current]):
            if visited[index] == False and not isinf(value):
                queue.append(index)
                visited[index] = True

    answer += 1

print(answer)
