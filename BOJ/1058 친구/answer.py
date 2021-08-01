import sys

input = sys.stdin.readline

count = int(input())

maps = {i: [float("inf")] * count for i in range(count)}

for i in range(count):
    relations = list(input().rstrip())

    for j in range(count):
        if i == j:
            maps[i][j] = 0
            continue

        # 선대칭으로 오기 때문에 j i 는 안해줘도 됨
        if relations[j] == "Y":
            maps[i][j] = 1

# 거치는 점
for i in range(count):
    # 시작점
    for j in range(count):
        # 끝점
        for k in range(count):
            if maps[j][k] > maps[j][i] + maps[i][k]:
                maps[j][k] = maps[j][i] + maps[i][k]

maximum = 0

for key in maps.keys():
    current = 0
    for j in maps[key]:
        if 1 <= j <= 2:
            current += 1

    maximum = max(maximum, current)

print(maximum)
