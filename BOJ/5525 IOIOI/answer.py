import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

S = input().strip()

answer = 0

index = 0

acc = 0

while index < M - 2:
    if (S[index] == "I") and S[index + 1] == "O" and S[index + 2] == "I":
        acc += 1

        if acc == N:
            answer += 1
            acc -= 1
        index += 2
    else:
        acc = 0
        index += 1


print(answer)
