import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, *B = map(int, input().split())

    avg = sum(B) / len(B)

    over_avg = 0

    for i in B:
        if i > avg:
            over_avg += 1

    print("{:.3f}%".format(over_avg / len(B) * 100))
