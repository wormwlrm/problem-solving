import sys
from collections import deque

input = sys.stdin.readline

S = int(input())

dp = [float("inf")] * (10_000 + 1)


def bfs(start):
    queue = deque([(start, 0)])

    visited = {}

    depth = -1

    while queue:
        depth += 1

        for _ in range(len(queue)):
            current, clipboard = queue.popleft()

            if (current, clipboard) in visited:
                continue

            visited[(current, clipboard)] = True

            dp[current] = min(dp[current], depth)

            if current == S:
                return dp[current]

            if clipboard != current:
                # 새로 복사하거나
                queue.append((current, current))

            # 클립보드에 뭐 들어있다면
            if clipboard > 0:
                # 붙여넣거나
                queue.append((current + clipboard, clipboard))

            # 지울 수 있다면
            if current > 1:
                queue.append((current - 1, clipboard))


answer = bfs(1)

print(answer)
