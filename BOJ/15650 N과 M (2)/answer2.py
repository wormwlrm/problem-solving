import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def combinations(arr, M):
    if M == 0:
        return [[]]
    elif M == 1:
        return [[item] for item in arr]

    result = []

    for index, value in enumerate(arr[: -M + 1 :]):
        for combo in combinations(arr[index + 1 : :], M - 1):
            result += [[value] + combo]

    return result


for combo in combinations(list(range(1, N + 1)), M):
    print(*combo)
