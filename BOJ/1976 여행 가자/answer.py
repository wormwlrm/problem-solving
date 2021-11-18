# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1976%20%EC%97%AC%ED%96%89%20%EA%B0%80%EC%9E%90

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

M = int(input())

area = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))

    for index, value in enumerate(line):
        if index + 1 == i:
            area[i][index + 1] = 0
        elif value == 0:
            area[i][index + 1] = float("inf")
        else:
            area[i][index + 1] = value


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if area[j][k] > area[j][i] + area[i][k]:
                area[j][k] = area[j][i] + area[i][k]


def valid():
    visit = list(map(int, input().split()))

    for index, value in enumerate(visit):
        if index == 0:
            continue

        if area[visit[index - 1]][value] == float("inf"):
            return False

    return True


print("YES" if valid() else "NO")
