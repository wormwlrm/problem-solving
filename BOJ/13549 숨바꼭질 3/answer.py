import sys
from collections import deque
from math import isinf

input = sys.stdin.readline

N, K = map(int, input().split())

MAXIMUM = 100_000

dp = [float("inf")] * (MAXIMUM + 1)


def teleport(start):
    current = start

    acc = []

    # 0에서 무한루프 돌지 않게
    if start == 0:
        return acc

    while current * 2 <= MAXIMUM:
        current *= 2
        acc.append(current)
        dp[current] = min(dp[current], dp[start])

    return acc


def dfs(start):
    # dp[start] = 0
    queue = deque([start, None])
    depth = 0

    while queue:
        current = queue.popleft()

        if current == None:
            if len(queue) == 0:
                return None

            depth += 1
            queue.append(None)
            continue

        # 정답 도착했다면
        if current == K:
            return min(dp[current], depth)

        # 방문한 적 있는 거는 더 작을 때만 갱신
        if not isinf(dp[current]) and dp[current] < depth:
            continue

        dp[current] = depth

        teleported = teleport(current)
        teleported_children = []

        for child in teleported:
            teleported_children.extend([min(MAXIMUM, child + 1), max(0, child - 1)])

        children = [
            min(MAXIMUM, current + 1),
            max(0, current - 1),
        ] + teleported_children

        for child in children:
            queue.append(child)


print(dfs(N))
