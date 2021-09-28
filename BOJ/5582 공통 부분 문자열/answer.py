import sys

input = lambda: sys.stdin.readline().rstrip()

S1 = input()

S2 = input()

prev_dp = [0] * (len(S2) + 1)

maximum = 0

for y in range(1, len(S1) + 1):
    current_char = S1[y - 1]

    current_dp = [0] * (len(S2) + 1)

    for x in range(1, len(S2) + 1):
        if S2[x - 1] == current_char:
            current_dp[x] = prev_dp[x - 1] + 1

    prev_dp = current_dp[::]

    maximum = max(maximum, max(current_dp))

print(maximum)
