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
        # arr 각 숫자에 대해 재귀로 순열을 추가
        for perm in permutation(arr[:index:] + arr[index + 1 : :], n - 1):
            result += [[elem] + perm]

    return result


combos = permutation(arr, M)

for combo in combos:
    key = str(combo)

    if key not in dic:
        print(*combo)
        dic[key] = 1
