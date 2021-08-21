import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

hash = {}

for index, value in enumerate(arr):
    if value not in hash:
        hash[value] = []

    hash[value].append(index)

for index, values in enumerate(sorted(hash.keys())):
    for value in hash[values]:
        arr[value] = index

print(*arr)
