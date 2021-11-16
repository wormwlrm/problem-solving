# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2688%20%EC%A4%84%EC%96%B4%EB%93%A4%EC%A7%80%20%EC%95%8A%EC%95%84

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    M = int(input())

    dp = {i: [0] * 11 for i in range(M + 1)}

    for j in range(10):
        dp[M][j] = 1

    for i in range(M - 1, -1, -1):
        dp[i][10] = 0

    for j in range(M - 1, -1, -1):
        for i in range(9, -1, -1):
            dp[j][i] = dp[j][i + 1] + dp[j + 1][i]

    print(dp[0][0])
