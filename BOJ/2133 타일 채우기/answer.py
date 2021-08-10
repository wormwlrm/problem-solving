import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

# 홀수면 경우의 수 없음
if N % 2 == 1:
    print(0)
else:
    blocks = [0] + [0, 3] + [0, 2] * 15
    dp = [[]]

    for i in range(1, 31):
        if i % 2 != 0:
            dp.append([])
            continue

        # 현재 블록 하나 넣어두고 선언
        current = [[i]]

        for k in range(2, i, 2):
            prev = deepcopy(dp[k])

            for j in prev:
                j.append(i - k)
                current.append(j)

        dp.append(current)

    acc = 0
    for method in dp[N]:
        multiply = 1
        for k in method:
            if k == 2:
                multiply *= 3
            else:
                multiply *= 2
        acc += multiply

    print(acc)
