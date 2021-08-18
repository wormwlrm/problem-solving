import sys

input = sys.stdin.readline

N = int(input())

cursor = list(map(int, input().split()))
smallest = min(cursor)

for i in range(1, N):
    arr = sorted(list(map(int, input().split())))
    j = N - 1

    while arr[j] > smallest:
        cursor.remove(smallest)
        cursor.append(arr[j])
        j -= 1
        smallest = min(cursor)

print(min(cursor))
