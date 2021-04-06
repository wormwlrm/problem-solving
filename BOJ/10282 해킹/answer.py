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


test_case = int(sys.stdin.readline().rstrip())

for test in range(test_case):
    computer_count, dependency_count, start_node = map(
        int, sys.stdin.readline().rstrip().split())

    graph = {i: {} for i in range(1, computer_count + 1)}

    for i in range(dependency_count):
        end, start, cost = map(int, sys.stdin.readline().rstrip().split())

        graph[start][end] = cost

    distances = dijkstra(graph, start_node)

    parasited_count = 0
    parasite_time = 0

    for i in distances:
        if (isinf(distances[i])):
            continue

        parasited_count += 1
        parasite_time = max(parasite_time, distances[i])

    print(parasited_count, parasite_time)
