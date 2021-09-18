import sys

input = sys.stdin.readline

X = input().strip()
Y = input().strip()

MAXIMUM = 1001

# 가로에 X, 세로에 Y 놓기
dp = [[0] * (len(X) + 1) for _ in range(len(Y) + 1)]

for y in range(1, len(Y) + 1):
    for x in range(1, len(X) + 1):
        ry, rx = y - 1, x - 1

        if X[rx] == Y[ry]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

# 끝점에서부터 거슬러 올라간다
cursor = (len(Y), len(X))
result = []

while True:
    cy, cx = cursor

    if cy == 0 or cx == 0:
        break

    # 대각선 방향으로 갈 수 있다면
    if Y[cy - 1] == X[cx - 1]:
        cursor = (cy - 1, cx - 1)
        result.append(Y[cy - 1])
        continue

    # 왼쪽이 더 큰 경우
    if dp[cy - 1][cx] < dp[cy][cx - 1]:
        cursor = (cy, cx - 1)
    # 오른쪽이 더 큰 경우
    else:
        cursor = (cy - 1, cx)

print(len(result))
if len(result) > 0:
    print("".join(result[::-1]))
