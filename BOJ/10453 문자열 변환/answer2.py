import sys

input = sys.stdin.readline

count = int(input())

for i in range(count):
    s1, s2 = map(str, input().rstrip().split())

    v1 = []
    v2 = []

    acc = 0

    for index, value in enumerate(s1):
        if value == "b":
            v1.append(index)

    for index, value in enumerate(s2):
        if value == "b":
            v2.append(index)

    for j in range(len(v1)):
        acc += abs(v1[j] - v2[j])

    print(acc)
