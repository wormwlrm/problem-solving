import sys

input = sys.stdin.readline

N, M = map(int, input().split())

d = [[float("inf") for _ in range(N)] for _ in range(N)]

for i in range(N):
    d[i][i] = 0

for _ in range(M):
    start, end = map(int, input().split())

    d[start - 1][end - 1] = 1
    d[end - 1][start - 1] = 1


# 중간
for i in range(N):
    # 시작
    for j in range(N):
        # 종료
        for k in range(N):
            if d[j][i] + d[i][k] < d[j][k]:
                d[j][k] = d[j][i] + d[i][k]

smallest_value = float("inf")
smallest_man = -1

for i in range(N):
    current = sum(d[i])
    if current < smallest_value:
        smallest_man = i + 1
        smallest_value = current

print(smallest_man)
