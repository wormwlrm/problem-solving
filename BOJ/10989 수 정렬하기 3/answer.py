import sys

input = sys.stdin.readline

count = int(input())

arr = [0] * 10001

for i in range(count):
    arr[int(input())] += 1

for i in range(10001):
    for _ in range(arr[i]):
        print(i)
