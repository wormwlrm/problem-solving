# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/15684%20%EC%82%AC%EB%8B%A4%EB%A6%AC%20%EC%A1%B0%EC%9E%91

import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, M, H = map(int, input().split())

ladder = [[0] * (N + 1) for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b] = 1

answer = float("inf")

available_points = {}

for h in range(H):
    for n in range(1, N):
        if ladder[h][n + 1] == 0 and ladder[h][n - 1] == 0 and ladder[h][n] == 0:
            available_points[(h, n)] = 1


def does_i_go_to_i():
    initial = list(range(1, N + 1))

    for row in range(H):
        for col in range(1, N):
            if ladder[row][col]:
                initial[col - 1], initial[col] = initial[col], initial[col - 1]

    return initial == list(range(1, N + 1))


answer = float("inf")

# 0개
if does_i_go_to_i():
    print(0)
    exit()


def is_valid_combo(points):
    temp = [[0] * (N + 1) for _ in range(H)]

    for point in points:
        py, px = point

        if temp[py][px] == 0 and temp[py][px - 1] == 0 and temp[py][px + 1] == 0:
            temp[py][px] = 1
        else:
            return False

    return True


for i in range(1, 4):
    combos = list(combinations(available_points.keys(), i))
    for points in list(combos):
        if is_valid_combo(points):
            for point in points:
                py, px = point
                ladder[py][px] = 1

            if does_i_go_to_i():
                print(i)
                exit()

            for point in points:
                py, px = point
                ladder[py][px] = 0

print(-1)
