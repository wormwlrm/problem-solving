import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    start, end, cost = map(int, input().split())

    if end not in graph[start]:
        graph[start][end] = cost
    else:
        # 중복되는 경로 있을 수 있으므로 최소값으로만 갱신
        graph[start][end] = min(graph[start][end], cost)

start, end = map(int, input().split())


def dijkstra(graph, start):
    distance = {node: float("inf") for node in graph}
    distance[start] = 0
    queue = []

    # 비용, 시작 노드
    heapq.heappush(queue, (distance[start], start))

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_cost > distance[current_node]:
            continue

        children = graph[current_node].keys()

        for child in children:
            if distance[child] > graph[current_node][child] + current_cost:
                distance[child] = graph[current_node][child] + current_cost
                heapq.heappush(queue, (distance[child], child))

    return distance


distance = dijkstra(graph, start)

print(distance[end])
