import sys
import math

input = sys.stdin.readline

# 최소 고객, 도시 갯수
C, N = map(int, input().split())

cities = []

for _ in range(N):
    cost, man = map(int, input().split())
    cities.append((cost, man))

current_cost = 0

# 나올 수 있는 최대 비용은 100원에 1명 나오는 조건에서 1000명 필요한 경우
maximum = 100 * 1000

# zero padding
dp = [0] + [0] * maximum


# 각 도시를 순회하면서 dp를 갱신하자
# 이때 비용 별로 구할 수 있는 최대 인원 대해 dp를 구해보자
# 즉 dp[비용] = 최대인원
for city in cities:
    # 도시 비용부터 시작, 모든 경우의 수 구함
    for cost in range(city[0], maximum + 1):
        # 현재 도시를 방문하기 위해서,
        # 현재 비용에서 도시 방문을 위한 비용을 뺌 (dp[cost - city[0]])
        # 그 후 도시를 방문함 (+ city[1])
        current = dp[cost - city[0]] + city[1]
        dp[cost] = max(dp[cost], current)

for index, value in enumerate(dp):
    if value >= C:
        print(index)
        break
