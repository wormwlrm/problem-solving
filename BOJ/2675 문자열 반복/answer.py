import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M, char = map(str, input().split())
    M = int(M)
    char = list(char)
    answer = ""
    for j in char:
        answer += j * M
    print(answer)
