import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

# zero padding
lands = [i for i in range(N + 2)]

occupied = [False for _ in range(N + 2)]

root = 1

for _ in range(Q):
    cursor = int(input())
    routes = [cursor]

    while cursor > 1:
        if cursor % 2 == 0:
            cursor //= 2
        else:
            cursor = (cursor - 1) // 2
        routes.append(cursor)

    routes.reverse()

    visitable = True
    for i in routes:
        if occupied[i] == True:
            visitable = False
            break

    if visitable:
        occupied[i] = True
        print(0)
    else:
        print(i)
