import sys

input = sys.stdin.readline

# 물건 갯수, 가방
N, K = map(int, input().split())

goods = [(0, 0)]

for _ in range(N):
    W, V = map(int, input().split())
    goods.append((W, V))

# 가로는 갯수, 세로는 무게
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 각 물건에 대해
for y in range(1, N + 1):
    # 무게에 대해
    for x in range(1, K + 1):
        weight, value = goods[y]

        # 담을 수 있음
        if weight <= x:
            # 위의 값 vs 지금 갖고 있는 물건의 무게를 뺀 거에 가치를 더한 거
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - weight] + value)
        # 가방 무게보다 물건이 무거워서 못 담음
        else:
            # 위의 값 가져옴
            dp[y][x] = dp[y - 1][x]

print(dp[N][K])
