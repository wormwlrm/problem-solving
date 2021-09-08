import sys

input = sys.stdin.readline

N = int(input())

numbers = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    current = numbers[i]

    maximum = -1

    # 자기보다 앞에 있는 수
    for j in range(i):
        if numbers[j] < current:
            maximum = max(maximum, dp[j])

    dp[i] = maximum + 1

print(max(dp))
