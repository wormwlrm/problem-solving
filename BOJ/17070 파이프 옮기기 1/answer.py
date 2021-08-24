import sys

input = sys.stdin.readline

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

# 가로, 대각선, 세로 방향
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

# 초기 파이프 설치
dp[0][0] = [1, 0, 0]
dp[0][1] = [1, 0, 0]


def get_left(y, x):
    try:
        # 현재 딛은 땅이 벽이거나, 왼쪽 땅이 벽인 경우
        if area[y][x] == 1 or area[y][x - 1] == 1:
            raise

        left = dp[y][x - 1]
    except:
        left = None
    return left


def get_diagonal(y, x):
    try:
        # 현재 딛은 땅이 벽이거나, 위, 왼쪽 땅이 벽인 경우
        if (
            area[y][x] == 1
            or area[y][x - 1] == 1
            or area[y - 1][x]
            or area[y - 1][x - 1]
        ):
            raise

        diagonal = dp[y - 1][x - 1]
    except:
        diagonal = None
    return diagonal


def get_up(y, x):
    try:
        # 현재 딛은 땅이 벽이거나, 위쪽 땅이 벽인 경우
        if area[y][x] == 1 or area[y - 1][x]:
            raise

        up = dp[y - 1][x]
    except:
        up = None
    return up


for y in range(N):
    # x가 0, 1인 경우는 방문 불가능
    for x in range(2, N):
        # 벽 만나면 그냥 패스
        if area[y][x] == 1:
            continue

        left = get_left(y, x)

        # 왼쪽 블럭에서는 가로, 대각선 방향에서만 접근 가능
        if left != None:
            dp[y][x][0] = left[0] + left[1]

        diagonal = get_diagonal(y, x)

        # 대각선 블럭은 모든 방향에서 접근 가능
        if diagonal != None:
            dp[y][x][1] = diagonal[0] + diagonal[1] + diagonal[2]

        up = get_up(y, x)

        # 세로 블럭은 대각선, 세로 방향에서 접근 가능
        if up != None:
            dp[y][x][2] = up[1] + up[2]

print(sum(dp[N - 1][N - 1]))
