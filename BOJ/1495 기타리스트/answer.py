import sys
from collections import deque

input = sys.stdin.readline

N, S, M = map(int, input().split())

volumes = list(map(int, input().split()))

queue = deque([S, None])
depth = 0
answer = -1


dp = [False] * (M + 1)


def get_availables():
    availables = []

    for index, value in enumerate(dp):
        if value == True:
            availables.append(index)

    return availables


while queue and depth <= N - 1:
    current = queue.popleft()

    if current == None:
        depth += 1
        for item in get_availables():
            queue.append(item)
        queue.append(None)

        # DP 초기화
        if depth <= N - 1:
            dp = [False] * (M + 1)
        continue

    volume = volumes[depth]

    if current + volume <= M:
        dp[current + volume] = True
    if current - volume >= 0:
        dp[current - volume] = True

for index, value in enumerate(dp):
    if value == True:
        answer = max(index, answer)

print(answer)
