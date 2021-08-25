import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N, R, Q = map(int, input().split())

connect = {i: [] for i in range(1, N + 1)}

children = {i: [] for i in range(1, N + 1)}

parents = {i: -1 for i in range(1, N + 1)}

size = {i: 0 for i in range(1, N + 1)}

for _ in range(N - 1):
    start, end = map(int, input().split())
    connect[start].append(end)
    connect[end].append(start)


def make_tree(current_node, parent):
    for node in connect[current_node]:
        if node != parent:
            parents[node] = current_node
            children[current_node].append(node)

            make_tree(node, current_node)


make_tree(R, -1)


def count_subtree_nodes(current_node):
    size[current_node] = 1
    for node in children[current_node]:
        count_subtree_nodes(node)
        size[current_node] += size[node]


count_subtree_nodes(R)

for _ in range(Q):
    print(size[int(input())])
