# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/16953%20A%20%E2%86%92%20B

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())


def bfs(start, target):
    dp = {start: float("inf")}

    turn = 0
    queue = deque([start])

    while queue:
        turn += 1

        for _ in range(len(queue)):
            current = queue.popleft()

            if current == target:
                return turn

            dp[current] = min(dp[current], turn)

            for child in [current * 2, current * 10 + 1]:
                if child <= B:
                    if child not in dp:
                        dp[child] = float("inf")

                    queue.append(child)

    return -1


print(bfs(A, B))
