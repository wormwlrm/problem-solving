import sys

input = sys.stdin.readline

N, K = map(int, input().split())

if (K) > (N / 2):
    K = N - K

jas = list(range(N, N - K, -1))

mos = list(range(1, K + 1))

DIVIDE = 10_007

answer = 1

ja = 1
mo = 1

for i in range(K):
    ja = ja * jas[i]
    mo = mo * mos[i]

print((ja // mo) % DIVIDE)
