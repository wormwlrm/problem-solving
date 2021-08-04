from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())

beads = list(map(int, input().split()))

numbers = list(range(1, N - 1))


def permutation(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        # arr 각 숫자에 대해 재귀로 순열을 추가
        for P in permutation(arr[:i:] + arr[i + 1 : :], n - 1):
            result += [[elem] + P]

    return result


def get_points(origin_arr, per):
    arr = origin_arr[::]
    points = 0

    while per:
        current = per[0]
        per = per[1::]

        points += arr[current - 1] * arr[current + 1]
        arr = arr[:current:] + arr[current + 1 : :]

        for i in range(len(per)):
            if per[i] > current:
                per[i] -= 1

    return points


perms = permutation(list(range(1, N - 1)), N - 2)

maximum = 0

for perm in perms:
    current = get_points(beads, perm)
    maximum = max(maximum, current)


print(maximum)
