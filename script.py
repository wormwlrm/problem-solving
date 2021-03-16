from collections import deque

n, k = map(int, (input().split()))

MAX = 100000
visited = [None] * (MAX + 1)

queue = deque([n, None])
depth = 0

if (k <= n):
    print(n - k)
else:
    while queue:
        current = queue.popleft()

        if (current == None):
            depth += 1
            queue.append(None)
            continue
        elif (current == k):
            break

        if visited[current] == None or depth < visited[current]:
            visited[current] = depth
            if (current - 1 >= 0):
                queue.append(current - 1)
            if (current + 1 <= MAX):
                queue.append(current + 1)
            if (current * 2 <= MAX):
                queue.append(current * 2)
    print(depth)
