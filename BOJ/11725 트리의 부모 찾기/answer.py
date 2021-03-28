import sys
from collections import deque

count = int(sys.stdin.readline().rstrip())

nodes = {}

parent = {
    1: 1
}

stack = deque([1])

for i in range(count - 1):
    f, t = map(int, sys.stdin.readline().rstrip().split())

    if f in nodes:
        nodes[f].add(t)
    else:
        nodes[f] = set([t])

    if t in nodes:
        nodes[t].add(f)
    else:
        nodes[t] = set([f])

while stack:
    current = stack.pop()

    children = list(nodes[current])

    for child in children:
        if child not in parent:
            parent[child] = current
            stack.append(child)


for i in range(2, count + 1):
    print(parent[i])
