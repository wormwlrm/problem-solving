# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/20114%20%EB%AF%B8%EC%95%84%20%EB%85%B8%ED%8A%B8

import sys

input = lambda: sys.stdin.readline().rstrip()

N, H, W = map(int, input().split())

strings = []

answer = []

for _ in range(H):
    strings.append(list((input())))

for i in range(N):
    guessed_char = "?"

    for y in range(H):
        for x in range(i * W, i * W + W):
            if strings[y][x] != "?":
                guessed_char = strings[y][x]
                break

    answer.append(guessed_char)

print("".join(answer))
