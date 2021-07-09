import sys
import heapq
from math import isinf

input = sys.stdin.readline

N = int(input())

graph = {i: {} for i in range(1, N + 1)}

start, end = map(int, input().split())

edges = int(input())

for i in range(1, edges + 1):
    man1, man2 = map(int, input().split())

    graph[man1][man2] = 1
    graph[man2][man1] = 1


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    q = []

    # 비용, 시작 노드를 튜플로 묶기
    heapq.heappush(q, (distances[start], start))

    while q:
        current_cost, current_node = heapq.heappop(q)

        if current_cost > distances[current_node]:
            continue

        for adj_node in graph[current_node].keys():
            if distances[adj_node] > graph[current_node][adj_node] + current_cost:
                distances[adj_node] = graph[current_node][adj_node] + current_cost
                heapq.heappush(q, (distances[adj_node], adj_node))

    return distances


distances = dijkstra(graph, start)

if isinf(distances[end]):
    print(-1)
else:
    print(distances[end])
