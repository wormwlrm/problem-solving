import sys
from collections import deque
from itertools import combinations
import math

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# zero padding
populations = [0] + list(map(int, input().split()))

graph = {i: [] for i in range(1, N + 1)}

for current in range(1, N + 1):
    count, *nearby = map(int, input().split())

    for near in nearby:
        graph[current].append(near)

combos = set([])

for i in range(1, (N // 2) + 1):
    for combo in combinations(range(1, N + 1), i):
        reverse = tuple([x for x in range(1, N + 1) if x not in combo])
        combos.add((combo, reverse))


def bfs(start, combo):
    queue = deque([start])
    visited = [None] + [False] * (N)
    visited[start] = True

    while queue:
        current = queue.popleft()

        for near in graph[current]:
            if not visited[near] and near in combo:
                visited[near] = True
                queue.append(near)

    for item in list(combo):
        if visited[item] == False:
            return False

    value = 0
    for item in combo:
        value += populations[item]

    return value


answer = float("inf")

for comb1, comb2 in combos:
    result1 = bfs(comb1[0], comb1)
    if result1 == False:
        continue

    result2 = bfs(comb2[0], comb2)
    if result2 == False:
        continue

    answer = min(answer, abs(result1 - result2))

if answer == float("inf"):
    print(-1)
else:
    print(answer)
