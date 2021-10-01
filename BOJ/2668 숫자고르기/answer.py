import sys

input = lambda: sys.stdin.readline().rstrip()

M = 100

dp = [None]
cycle_dp = [None]

N = int(input())

for _ in range(N):
    dp.append(int(input()))
    cycle_dp.append(set([]))


def traversal(start):
    visited = [False] * (N + 1)

    current = start

    while True:
        current = dp[current]

        # 처음 자기 자신 값으로 돌아온거면 사이클임
        if current == start:
            visited[start] = True
            break

        # 자기 자신으로 돌아온 거 아닌데 사이클 있는 거면 불필요한 노드 있다는 뜻
        if visited[current] == True:
            if len(cycle_dp[current]) == 0:
                visited = traversal(current)
            else:
                return cycle_dp[current]
            break

        visited[current] = True

    cycle = []

    for index, value in enumerate(visited):
        if index == 0:
            continue

        if value == True:
            cycle.append(index)

    cycle_dp[start] = set(cycle)

    return cycle


cycles = set([])

for i in range(1, N + 1):
    if i in cycles:
        continue

    cycle = traversal(i)
    for c in cycle:
        cycles.add(c)

print(len(cycles))

for i in sorted(cycles):
    print(i)

