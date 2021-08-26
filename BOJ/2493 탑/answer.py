import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dp = [0] * N

towers = list(map(int, input().split()))

indexes = deque([1])
heights = deque([towers[0]])

for index in range(1, N):
    while True:
        # 다 뺀 거면 최대 높이 갱신하고 끝
        if len(heights) == 0:
            indexes.append(index + 1)
            heights.append(towers[index])
            dp[index] = 0
            break

        # 작으면 다 뺌
        if towers[index] > heights[-1]:
            indexes.pop()
            heights.pop()
        # 크면 표시
        else:
            dp[index] = indexes[-1]

            indexes.append(index + 1)
            heights.append(towers[index])
            break


print(*dp)
