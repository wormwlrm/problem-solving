# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2098%20%EC%99%B8%ED%8C%90%EC%9B%90%20%EC%88%9C%ED%9A%8C

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [[float("inf")] * (1 << N) for _ in range(N)]

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

# visited는 이진수
# 0101 = 2번째, 0번째 도시 방문함
def dfs(x, visited):
    # 모든 도시 방문
    if visited == (1 << N) - 1:
        # x에서 0으로 가는 경로 있을 때
        if graph[x][0]:
            return graph[x][0]
        else:
            float("inf")

    if dp[x][visited] != float("inf"):
        return dp[x][visited]

    # 모든 노드 탐방
    for node in range(1, N):
        # 이어져 있지 않다면
        if not graph[x][node]:
            continue
        # 이미 방문한 도시
        if visited & (1 << node):
            continue

        dp[x][visited] = min(
            dp[x][visited], 
            # visited에 or 연산으로 현재 방문한 노드 추가
            # 비용도 추가
            dfs(node, visited | (1 << node)) + graph[x][node]
        )

    return dp[x][visited]


print(dfs(0, 1))
