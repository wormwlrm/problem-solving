from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])

removed = deque([])

index = k - 1

while True:
    removed.append(str(queue[index]))
    del queue[index]

    if (not queue):
        break
    index = ((index - 1) + k) % len(queue)

print('<', end='')
print(', '.join(list(removed)), end='')
print('>')
