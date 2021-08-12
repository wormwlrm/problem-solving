import sys

input = sys.stdin.readline

N, M = map(int, input().split())

holidays = list(map(int, input().split()))

# 가로는 날짜, 세로는 쿠폰 갯수
# 최대 100일까지 이용 가능한데 제일 마지막에 5일짜리 쓸 수 있으니까 105
# 쿠폰은 최대 40개까지 저장 가능
dp = [[float("inf") for _ in range(45)] for _ in range(110)]

dp[0][0] = 0

# 전체 날짜
for day in range(N + 1):
    for coupon in range(41):
        # 가격
        current = dp[day][coupon]

        # 다음날 휴일인 경우, 전날꺼 그대로 가져오면 됨
        if day + 1 in holidays:
            dp[day + 1][coupon] = min(current, dp[day + 1][coupon])

        # 쿠폰 3개 이상인 경우 다음 날은 공짜로 하루 쓰기
        if coupon >= 3:
            dp[day + 1][coupon - 3] = min(current, dp[day + 1][coupon - 3])

        # 1일권
        dp[day + 1][coupon] = min(current + 10000, dp[day + 1][coupon])

        # 3일권
        for i in range(1, 4):
            dp[day + i][coupon + 1] = min(current + 25000, dp[day + i][coupon + 1])

        # 5일권
        for i in range(1, 6):
            dp[day + i][coupon + 2] = min(current + 37000, dp[day + i][coupon + 2])


print(min(dp[N]))
