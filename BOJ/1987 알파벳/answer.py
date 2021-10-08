import sys

input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())

area = []

for _ in range(R):
    line = list(input().rstrip())
    area.append(line)


maximum = -float("inf")


def bfs(y, x, turn):
    global maximum, collected

    maximum = max(maximum, turn)

    for ty, tx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        chy = y + ty
        chx = x + tx

        if 0 <= chy < R and 0 <= chx < C:
            current = ord(area[chy][chx]) - 65

            if collected[current] == False:
                collected[current] = True
                bfs(chy, chx, turn + 1)
                collected[current] = False


collected = [False] * 26
first = ord(area[0][0]) - 65
collected[first] = True

bfs(0, 0, 1)

print(maximum)
