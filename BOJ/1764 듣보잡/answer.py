import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dict = {}

for i in range(N):
    name = input().rstrip()
    dict[name] = True

answer = []

for i in range(M):
    name = input().rstrip()
    if name in dict:
        answer.append(name)

print(len(answer))

for i in sorted(answer):
    print(i)
