import sys

input = sys.stdin.readline

N, D, K, C = map(int, input().split())

table = []

for _ in range(N):
    table.append(int(input()))

maximum = 0

for i in range(N):
    indexes = []
    for index in range(i, i + K):
        indexes.append(index % N)

    current_dishes = [0] * (D + 1)
    current_dishes[C] = 1

    for index in indexes:
        current_dishes[table[index]] = 1

    total_kinds = current_dishes.count(1)

    maximum = max(maximum, total_kinds)

print(maximum)
