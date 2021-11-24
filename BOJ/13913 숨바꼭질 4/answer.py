# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/13913%20%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%204

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 가는데 걸리는 시간
dp = [float("inf")] * 200_001

N, K = map(int, input().split())

queue = deque([(-1, N)])
dp[N] = 0
depth = -1

prev = [None] * 200_001


def bfs():
    global depth

    while queue:
        depth += 1

        for _ in range(len(queue)):
            previous, current = queue.popleft()

            if dp[current] < depth:
                continue

            dp[current] = depth
            prev[current] = previous

            if current == K:
                return

            if current > 0:
                # 이전 칸
                if dp[current - 1] > depth:
                    queue.append((current, current - 1))

            if current * 2 <= 200_000:
                # 다음 칸
                if dp[current + 1] > depth:
                    queue.append((current, current + 1))

                # 두 배 칸
                if dp[current * 2] > depth:
                    queue.append((current, current * 2))


bfs()

print(dp[K])

answer = []
index = K
while index != -1:
    answer.append(index)
    index = prev[index]

answer.reverse()

print(*answer)
