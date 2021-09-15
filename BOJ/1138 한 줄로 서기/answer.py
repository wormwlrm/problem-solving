from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())

order = list(map(int, input().split()))

first_index = order[0]

if N == 1:
    print(1)
    exit()

cases = list(permutations(range(2, N + 1), N - 1))


def is_answer(case):
    dp = [0] * N

    for i in range(N):
        now = case[i]

        acc = 0

        for j in range(i):
            if case[j] > now:
                acc += 1

        dp[now - 1] = acc

    return True if dp == order else False


for case in cases:
    case = list(case)
    case.insert(first_index, 1)

    if is_answer(case):
        print(" ".join(map(str, case)))
        break
