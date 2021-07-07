import sys

input = sys.stdin.readline

count = int(input())

days = []

pays = []

dp = [0]

for i in range(count):
    day, pay = map(int, input().rstrip().split())

    days.append(day)
    pays.append(pay)

# 마지막날로부터 거꾸로 탐색
for i in range(count - 1, -1, -1):
    today = i

    # 오늘부터 시작할 수 있는 일이 퇴사날을 넘기면 스킵
    if today + days[today] > count:
        dp.append(dp[-1])
        continue

    # 만약 오늘 일을 한다면 얼마나 받을까?
    pay_today = pays[today]
    # 만약 오늘 일을 한다면 며칠 걸릴까?
    cost_today = days[today]
    # 만약 오늘 일을 한다면, 며칠을 기준으로 DP를 계산할까?
    # 오늘 할 일에 걸리는 시간 `cost_today` 까지 계산한 거
    day_remain = (count - today) - cost_today

    # (오늘 할 일 + 오늘 할 일만큼 걸리는 시간까지의 DP) vs 그냥 일 안한 거
    if pay_today + dp[day_remain] > (dp[-1] + 0):
        dp.append(pay_today + dp[day_remain])
    #
    else:
        dp.append(dp[-1])

print(dp[-1])
