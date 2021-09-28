import sys

input = lambda: sys.stdin.readline().rstrip()

S1 = input()

S2 = input()

dp = [[0] * (len(S1) + 1) for _ in range(len(S2) + 1)]

for y in range(1, len(S2) + 1):
    for x in range(1, len(S1) + 1):
        if S1[x - 1] == S2[y - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1

maximum = 0

for line in dp:
    maximum = max(maximum, max(line))

print(maximum)
