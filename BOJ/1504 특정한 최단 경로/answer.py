# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1504%20%ED%8A%B9%EC%A0%95%ED%95%9C%20%EC%B5%9C%EB%8B%A8%20%EA%B2%BD%EB%A1%9C

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N, E = map(int, input().split())

graph = {i: {} for i in range(1, N + 1)}

for _ in range(E):
    a, b, cost = map(int, input().split())

    graph[a][b] = cost
    graph[b][a] = cost

via1, via2 = map(int, input().split())


def dijkstra(graph, start):
    distance = {i: float("inf") for i in graph.keys()}
    distance[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))

    while queue:
        cost, node = heapq.heappop(queue)

        for adj in graph[node]:
            if distance[adj] > cost + graph[node][adj]:
                distance[adj] = cost + graph[node][adj]
                heapq.heappush(queue, (distance[adj], adj))

    return distance


answer = float("inf")

start = 1
end = N

for v1, v2 in [[via1, via2], [via2, via1]]:
    current_cost = 0

    distance1 = dijkstra(graph, start)
    current_cost += distance1[v1]

    distance2 = dijkstra(graph, v1)
    current_cost += distance2[v2]

    distance3 = dijkstra(graph, v2)
    current_cost += distance3[end]

    answer = min(answer, current_cost)

print(-1 if answer == float("inf") else answer)
