import sys

input = sys.stdin.readline

N = int(input())


for _ in range(N):
    sequence = 1
    acc = 0
    OX = list(input().rstrip())

    for char in OX:
        if char == "O":
            acc += sequence
            sequence += 1
        else:
            sequence = 1

    print(acc)
