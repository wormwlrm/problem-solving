from queue import Queue

computer_count = int(input())
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

queue = Queue()
queue.put(1)

while not queue.empty():
    n = queue.get()
    if (n not in visited):
        visited.append(n)
        child = list(set(nodes[n]) - set(visited))
        for i in child:
            queue.put(i)

print(len(visited) - 1)
