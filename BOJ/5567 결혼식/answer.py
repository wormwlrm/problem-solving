from collections import deque

friend_count = int(input())
node_count = int(input())

nodes = {}
visited = []

for i in range(node_count):
    f, t = map(int, input().split())

    if f in nodes:
        nodes[f].add(t)
    else:
        nodes[f] = set([t])

    if t in nodes:
        nodes[t].add(f)
    else:
        nodes[t] = set([f])


def recursive(current, dep):
    if (dep > 2):
        return

    if (current not in visited):
        visited.append(current)

    child = list(set(nodes[current]) - set(visited))

    for i in child:
        recursive(i, dep + 1)


recursive(1, 0)


print(len(visited) - 1)
