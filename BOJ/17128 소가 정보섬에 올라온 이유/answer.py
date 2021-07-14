import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

qualities = list(map(int, input().split()))

jokes = list(map(int, input().split()))

multiply = [1 for _ in range(N)]

for i in range(N):
    index1 = (i) % N
    index2 = (i + 1) % N
    index3 = (i + 2) % N
    index4 = (i + 3) % N
    multiply[i] = (
        qualities[index1] * qualities[index2] * qualities[index3] * qualities[index4]
    )

old_sum = sum(multiply)

for joke in jokes:
    index1 = (joke - 1 - 3) % N
    index2 = (joke - 1 - 2) % N
    index3 = (joke - 1 - 1) % N
    index4 = (joke - 1) % N

    multiply[index1] *= -1
    multiply[index2] *= -1
    multiply[index3] *= -1
    multiply[index4] *= -1

    acc = multiply[index1] + multiply[index2] + multiply[index3] + multiply[index4]
    old_sum += acc * 2

    print(old_sum)
