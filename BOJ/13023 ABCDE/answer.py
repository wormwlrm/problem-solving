import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = {i: [] for i in range(N)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, visited, depth):
    global graph

    visited[start] = True

    if depth == 5:
        print(1)
        exit()

    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited, depth + 1)

    visited[start] = False


depth = 1

for start in range(N):
    visited = [False] * N
    dfs(start, visited, depth)

print(0)
