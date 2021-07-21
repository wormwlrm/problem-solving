import sys

input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

hash = {}

acc = []

for number in numbers:
    temp = []
    for index, value in enumerate(acc):
        temp.append(acc[index] + number)
    temp.append(number)

    for i in temp:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    acc = acc + temp[::]


if S in hash:
    print(hash[S])
else:
    print(0)
