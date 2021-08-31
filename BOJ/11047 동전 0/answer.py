import sys

input = sys.stdin.readline

N, K = map(int, input().split())

charge = [int(input()) for _ in range(N)]

count = [0] * N

cursor = N - 1

remain = K

while remain > 0:
    if charge[cursor] > remain:
        cursor -= 1
        continue

    share = remain // charge[cursor]
    count[cursor] = share
    remain -= share * charge[cursor]

print(sum(count))
