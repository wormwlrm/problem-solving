import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

connects = list(map(int, input().split()))

parents = {i: -1 for i in range(N)}

children = {i: [] for i in range(N)}

for index, value in enumerate(connects):
    parents[index] = value

    if value != -1:
        children[value].append(index)

target = int(input())

# target의 children을 구함
queue = deque([target])

while queue:
    current = queue.popleft()

    for child in children[current]:
        if child != None:
            queue.append(child)

    children[current] = None
    parents[current] = None

answer = 0
for key in children.keys():
    if children[key] == None:
        continue

    if target in children[key]:
        children[key].remove(target)

    if len(children[key]) == 0:
        answer += 1

print(answer)
