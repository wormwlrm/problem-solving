nodes = {}
visited = []
current = {}
parent = {}
stack = []

children = list(set(nodes[current] - set(visited)))

for child in children:
    parent[child] = current
    stack.append(child)


children = list(nodes[current])

for child in children:
    if child not in parent:
        parent[child] = current
        stack.append(child)
