import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [0] + list(map(int, input().split()))

acc = [0]

for i in range(1, N + 1):
    acc.append(acc[i - 1] + numbers[i])

for _ in range(M):
    start, end = map(int, input().split())

    print(acc[end] - acc[start - 1])
