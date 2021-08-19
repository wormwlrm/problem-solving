import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

edge = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)
    edge[end].append(start)


def dfs(start):
    visited = [False] * (N + 1)
    stack = deque([start])

    answer = []

    while stack:
        current = stack.pop()

        if visited[current] == True:
            continue

        visited[current] = True
        answer.append(current)

        children = sorted(edge[current], reverse=True)

        for child in children:
            if visited[child] == False:
                stack.append(child)

    return answer


def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    answer = []

    while queue:
        current = queue.popleft()
        answer.append(current)

        children = sorted(edge[current])

        for child in children:
            if visited[child] == False:
                queue.append(child)
                visited[child] = True

    return answer


print(*dfs(V))
print(*bfs(V))
