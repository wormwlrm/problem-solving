from math import inf
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

distance = {i: {} for i in range(1, V + 1)}

for _ in range(E):
    start, end, cost = map(int, input().split())

    if end not in distance[start]:
        distance[start][end] = float("inf")

    distance[start][end] = min(distance[start][end], cost)


for i in range(1, V + 1):
    distance[i][i] = 0


def dijkstra(graph, start):
    distance = {i: inf for i in range(1, V + 1)}
    distance[start] = 0

    queue = []
    # 비용, 시작 노드를 튜플로 묶기
    heapq.heappush(queue, (graph[start][start], start))

    while queue:
        cost, position = heapq.heappop(queue)

        for key in graph[position]:
            if distance[key] > cost + graph[position][key]:
                distance[key] = cost + graph[position][key]
                heapq.heappush(queue, (distance[key], key))

    return distance


distance = dijkstra(distance, K)

for value in distance.values():
    if value == inf:
        print("INF")
    else:
        print(value)
