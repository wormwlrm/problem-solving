import heapq

vertex_count = int(input())
edge_count = int(input())

edges = []

# 0번째 때문에 인덱스 에러 나는 것 방지하기 위해 zero-padding
parent = [i for i in range(vertex_count + 1)]

weight = 0

current_edge = 0

for i in range(edge_count):
    f, t, cost = map(int, input().split())
    edges.append((f, t, cost))

edges.sort(key=lambda x: x[2])


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return find(parent[x])


def union(x, y):
    '''
    x와 y를 연결, 노드 숫자 작은 거를 부모로
    '''
    x_root = find(x)
    y_root = find(y)

    if (x_root == y_root):
        return

    if (x_root < y_root):
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


for edge in edges:
    if (current_edge == edge_count):
        break

    f, t, cost = edge

    if (find(t) == find(f)):
        continue
    else:
        weight += cost
        current_edge += 1
        union(f, t)

print(weight)
