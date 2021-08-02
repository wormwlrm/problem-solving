import sys

input = sys.stdin.readline

N = int(input())

MAXIMUM = 301

steps = [0] * MAXIMUM

# 값, 경로
dp = [[(0, [])]] + [] * MAXIMUM

for i in range(1, N + 1):
    steps[i] = int(input())

dp.append([(steps[1], [1])])

for i in range(2, N + 1):
    temp = []

    # 이전 값에서 +1 한 것
    previous = dp[i - 1]

    temp1 = (0, [])
    temp2 = (0, [])

    for prev in previous:
        value, route = prev
        # 111, 211은 걸러야 함
        if len(route) >= 2 and route[-2::] in [[1, 1], [2, 1]]:
            continue

        if temp1[0] < value + steps[i]:
            temp1 = (value + steps[i], route + [1])

    # 이이전 값에서 +2 한 것
    previous2 = dp[i - 2]

    for prev2 in previous2:
        value, route = prev2

        if temp2[0] < value + steps[i]:
            temp2 = (value + steps[i], route + [2])

    dp.append([temp1, temp2])

answers = dp[N]

maximum = 0
for value, route in answers:
    maximum = max(maximum, value)

print(maximum)
