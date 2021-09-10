import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))


def combinations(arr, M):
    if M == 0:
        return [[]]

    elif M == 1:
        return [[item] for item in arr]

    result = []

    for index, value in enumerate(arr[::]):
        for combo in combinations(arr[index::], M - 1):
            result += [[value] + combo]

    return result


combos = combinations(arr, M)

for combo in combos:
    print(*combo)
