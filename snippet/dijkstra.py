from math import inf
import heapq


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
