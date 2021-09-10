import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

dic = {}


def permutation(arr, n):
    result = []

    if n == 0:
        return [[]]

    for index, elem in enumerate(arr):
        for perm in permutation(arr[index::], n - 1):
            result += [[elem] + perm]

    return result


combos = permutation(arr, M)

for combo in combos:
    key = str(combo)

    if key not in dic:
        print(*combo)
        dic[key] = 1
