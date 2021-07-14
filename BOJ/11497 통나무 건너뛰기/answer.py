import sys

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    log_count = int(input())

    logs = sorted(list(map(int, input().split())))

    max_diff = 0

    acc = []

    for index, value in enumerate(logs):
        if index == 0:
            acc.append(value)
            continue

        acc.append(value)

        index_to_calc = max(index - 2, 0)
        max_diff = max(max_diff, abs(acc[index] - acc[index_to_calc]))

    max_diff = max(max_diff, abs(acc[-1] - acc[-2]))

    print(max_diff)
