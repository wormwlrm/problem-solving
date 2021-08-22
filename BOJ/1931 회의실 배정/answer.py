import sys

input = sys.stdin.readline

N = int(input())

studies = []

for _ in range(N):
    start, end = map(int, input().split())
    studies.append((start, end))

studies.sort(key=lambda x: (x[1], x[0]))

last_end = 0

answer = 0

for study in studies:
    start, end = study

    if last_end <= start:
        answer += 1
        last_end = end

print(answer)
