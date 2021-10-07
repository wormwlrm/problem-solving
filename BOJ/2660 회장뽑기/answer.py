import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())


def floyd(distance):
    # 중간
    for i in range(1, N + 1):
        # 시작
        for j in range(1, N + 1):
            # 도착
            for k in range(1, N + 1):
                if (distance[j][i] + distance[i][k]) < distance[j][k]:
                    distance[j][k] = distance[j][i] + distance[i][k]

    return distance


# zero padding
distance = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    distance[i][i] = 0

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    distance[a][b] = 1
    distance[b][a] = 1

distance = floyd(distance)

point, candidate_count = float("inf"), 0

candidates = []

for i in range(1, N + 1):
    current_point = max(distance[i][1::])

    if current_point > point:
        continue
    elif current_point < point:
        point = current_point
        candidate_count = 1
        candidates = [i]
    else:
        candidate_count += 1
        candidates.append(i)


print(point, candidate_count)
print(*sorted(candidates))
