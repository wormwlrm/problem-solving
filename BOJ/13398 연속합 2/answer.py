# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/13398%20%EC%97%B0%EC%86%8D%ED%95%A9%202

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

numbers = list(map(int, input().split()))

# dp1은 연속된 숫자를 고르는 경우, N번째까지 고른 경우에서 가장 큰 값
dp_1 = [numbers[0]]

for i in range(1, N):
    # dp_1[i - 1] + numbers[i]: 이전까지의 누적값 + 현재값
    # numbers[i]: 단순 현재값, 위 값이 음수일 수 있기 때문
    maximum = max(dp_1[i - 1] + numbers[i], numbers[i])
    dp_1.append(maximum)


## dp2는 숫자 1개를 뺀 경우
dp_2 = []

# 3개부터 의미 있음
if len(numbers) > 2:
    dp_2.append(dp_1[0])

    for i in range(2, len(numbers)):
        # dp_1[i - 2] + numbers[i]: i-2번째까지의 최대값 + 현재값, 즉 i-1번째를 뺀 거
        # dp_2[-1] + numbers[i]: 이전에 i-1번째가 제거된 값 + 현재값, 즉 i-N번째가 빠진 값
        maximum = max(dp_1[i - 2] + numbers[i], dp_2[-1] + numbers[i])
        dp_2.append(maximum)


print(max(dp_1 + dp_2))
