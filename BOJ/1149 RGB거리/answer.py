import sys

input = sys.stdin.readline

N = int(input())

dp = [0, 0, 0]

red1, green1, blue1 = map(int, input().split())
red2, green2, blue2 = map(int, input().split())

dp[0] = min(green1, blue1) + red2
dp[1] = min(red1, blue1) + green2
dp[2] = min(red1, green1) + blue2


for _ in range(2, N):
    red, green, blue = map(int, input().split())

    temp = [0, 0, 0]

    temp[0] = min(dp[1], dp[2]) + red
    temp[1] = min(dp[0], dp[2]) + green
    temp[2] = min(dp[0], dp[1]) + blue

    dp = temp

print(min(dp))
