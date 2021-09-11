import sys
from math import isinf

input = sys.stdin.readline

N = int(input())

M = int(input())

distance = [[float("inf")] * (N) for _ in range(N)]

for x in range(N):
    distance[x][x] = 0

for _ in range(M):
    start, end, cost = map(int, input().split())
    distance[start - 1][end - 1] = min(distance[start - 1][end - 1], cost)

for i in range(N):
    for j in range(N):
        for k in range(N):
            if distance[j][i] + distance[i][k] < distance[j][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

for y in range(N):
    for x in range(N):
        if isinf(distance[y][x]):
            distance[y][x] = 0

for line in distance:
    print(*line)
