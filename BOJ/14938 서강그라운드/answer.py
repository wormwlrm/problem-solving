import sys
from math import inf, isinf
import heapq


def dijkstra(graph, start):
    distance = {f: inf for f in graph}
    distance[start] = 0

    queue = []

    # 비용, 시작 노드를 튜플로 묶기
    heapq.heappush(queue, (distance[start], start))

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        for adj_node in graph[current_node].keys():
            if (distance[adj_node] > current_cost + graph[current_node][adj_node]):
                distance[adj_node] = current_cost + \
                    graph[current_node][adj_node]

                heapq.heappush(queue, (distance[adj_node], adj_node))

    return distance


location_count, detectable_range, road_count = map(
    int, sys.stdin.readline().rstrip().split())

items = list(map(int, sys.stdin.readline().rstrip().split()))

item_graph = {}

for index, value in enumerate(items):
    item_graph[index + 1] = value


graph = {i: {} for i in range(1, location_count + 1)}

for i in range(road_count):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())

    graph[start][end] = cost
    graph[end][start] = cost

max_item_count = 0

for i in range(1, location_count + 1):
    distances = dijkstra(graph, i)

    current_item_count = 0

    for j in distances:
        if (distances[j] <= detectable_range):
            current_item_count += item_graph[j]

    max_item_count = max(current_item_count, max_item_count)

print(max_item_count)
