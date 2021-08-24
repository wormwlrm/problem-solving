import sys

input = sys.stdin.readline

N = int(input())

answer = []

for i in range(N):
    if i == 0:
        answer = list(input().strip())
        continue

    command = input().strip()

    for j in range(len(command)):
        if command[j] == answer[j]:
            continue
        else:
            answer[j] = "?"

print("".join(answer))
