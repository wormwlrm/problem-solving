# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/14732%20%ED%96%89%EC%82%AC%EC%9E%A5%20%EB%8C%80%EC%97%AC%20(Small)

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

area = [[0] * 500 for _ in range(500)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = 1

print(sum(sum(area[i]) for i in range(500)))
