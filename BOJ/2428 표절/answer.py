import math

count = int(input())

files = sorted(list(map(float, input().split())))


def binary_search(value, index):
    left = 0
    right = index

    while (left <= right):
        mid = (left + right) // 2
        current = files[mid]

        if (current < value * 0.9):
            left = mid + 1
        elif (current > value * 0.9):
            right = mid - 1
        else:
            right = mid - 1

    return index - left


result = 0

for index, value in enumerate(files):
    if (index == 0):
        continue
    result += binary_search(value, index)

print(result)
