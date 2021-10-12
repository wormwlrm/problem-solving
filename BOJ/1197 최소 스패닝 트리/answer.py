# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1197%20%EC%B5%9C%EC%86%8C%20%EC%8A%A4%ED%8C%A8%EB%8B%9D%20%ED%8A%B8%EB%A6%AC

import sys

input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())

# 처음 부모는 자기 자신 가리키게
parents = {i: i for i in range(1, V + 1)}

edges = []

for _ in range(E):
    A, B, C = map(int, input().split())

    # 가중치 기준 정렬
    edges.append((C, A, B))


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    if find(x) == find(y):
        return

    if x > y:
        x, y = y, x

    parents[find(y)] = find(x)


edges.sort(key=lambda x: x[0])

edge_count = 0

acc = 0

for weight, A, B in edges:
    if find(A) != find(B):
        union(A, B)
        edge_count += 1
        acc += weight

        if edge_count == V - 1:
            break

print(acc)
