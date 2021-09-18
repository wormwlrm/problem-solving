import sys
from collections import deque
from math import isinf

input = sys.stdin.readline

# 건물 층, 출발지, 목적지, 위로, 아래로
F, S, G, U, D = map(int, input().split())

dp = [float("inf")] * (F + 1)


def get_children(position):
    children = []

    # 위층으로 가기
    up = position + U

    # position이 F인 경우는 제외해서 무한 반복 제거
    if up <= F and isinf(dp[up]):
        children.append(up)

    # 아래층으로 가기
    down = position - D

    # position이 1인 경우는 제외해서 무한 반복 제거
    if 1 <= down and isinf(dp[down]):
        children.append(down)

    return children


def dfs(S):
    queue = deque([S])

    depth = -1

    while queue:
        depth += 1

        for _ in range(len(queue)):
            current = queue.popleft()

            # 이미 방문한 적 있다면
            if not isinf(dp[current]):
                continue

            dp[current] = depth

            if current == G:
                return depth

            children = get_children(current)

            for child in children:
                if isinf(dp[child]):
                    queue.append(child)

    return None


result = dfs(S)

if result == None:
    print("use the stairs")
else:
    print(result)
