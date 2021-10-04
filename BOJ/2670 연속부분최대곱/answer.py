import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(float(input()))

dp = [1] * (N)

dp[0] = numbers[0]

for i in range(1, N):
    # 이전까지 곱한게 1보다 크면 계속 곱하기
    if dp[i - 1] > 1:
        dp[i] = dp[i - 1] * numbers[i]
    # 이전까지 곱한게 1보다 작다면 현재꺼에서 다시 시작하기
    else:
        dp[i] = numbers[i]


print("{0:.3f}".format(max(dp)))
