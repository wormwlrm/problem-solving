import sys

input = sys.stdin.readline

N, H = map(int, input().split())

ceil = [0] * (H + 1)
floor = [0] * (H + 1)

heights = [float("inf")] + [0] * H

for i in range(N):
    current = int(input())

    # 석순, 밑에서부터
    if i % 2 == 0:
        floor[current] += 1

    # 종유석, 위에서부터
    else:
        ceil[H - current + 1] += 1

# 석순은 위에서부터 탐색
acc = 0
for i in range(H, 0, -1):
    heights[i] += floor[i] + acc
    acc += floor[i]

# 종유석은 밑에서부터 탐색
acc = 0
for i in range(1, H + 1):
    heights[i] += ceil[i] + acc
    acc += ceil[i]

min_value = min(heights)

print(min_value, heights.count(min_value))
