# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1707%20%EC%9D%B4%EB%B6%84%20%EA%B7%B8%EB%9E%98%ED%94%84

import sys

sys.setrecursionlimit(10 ** 9)


input = lambda: sys.stdin.readline().rstrip()

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = {i: [] for i in range(1, V + 1)}

    for _ in range(E):
        u, v = map(int, input().split())

        if u == v:
            continue

        graph[u].append(v)
        graph[v].append(u)

    visited = {i: None for i in range(1, V + 1)}

    def dfs(start, turn):
        visited[start] = turn

        for adj in graph[start]:
            if visited[adj] == None:
                result = dfs(adj, turn + 1)

                if result == False:
                    return result
            else:
                cycle_count = turn - visited[adj]

                # 홀수만큼 순환이 일어났으면
                if cycle_count > 1 and cycle_count % 2 == 0:
                    return False

    answer = True

    for i in range(1, V + 1):
        if visited[i] == None:
            answer = dfs(i, 1)

        if answer == False:
            break

    print("YES" if answer == None else "NO")
