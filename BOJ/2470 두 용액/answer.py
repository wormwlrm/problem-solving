import sys

input = sys.stdin.readline

N = int(input())

ph = list(map(int, input().split()))

ph.sort()

left = 0
right = N - 1

minimum = float("inf")
min_left = left
min_right = right

while left < right:
    current = ph[left] + ph[right]

    if abs(current) < abs(minimum):
        minimum = current
        min_left = left
        min_right = right

    if current > 0:
        right -= 1
    elif current < 0:
        left += 1
    else:
        break


print(ph[min_left], ph[min_right])
