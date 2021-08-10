import sys
from math import isinf

input = sys.stdin.readline

N = int(input())

maps = {i: [float("inf")] * N for i in range(N)}

for i in range(N):
    line = list(map(int, input().split()))

    for j in range(N):

        # 갈 수 있으면 비용 1로 만들기
        if line[j] == 1:
            maps[i][j] = 1


# 거치는 점
for i in range(N):
    # 시작점
    for j in range(N):
        # 끝점
        for k in range(N):
            if maps[j][k] > maps[j][i] + maps[i][k]:
                maps[j][k] = maps[j][i] + maps[i][k]


for i in range(N):
    temp = []
    for j in range(N):
        if isinf(maps[i][j]):
            temp.append(0)
        else:
            temp.append(1)
    print(*temp)
