import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    case = int(input())

    dress = {}

    for _ in range(case):
        name, kind = map(str, input().strip().split())

        if kind not in dress:
            dress[kind] = 0

        dress[kind] += 1

    if len(dress.keys()) == 0:
        print(0)
        continue
    elif len(dress.keys()) == 1:
        print(dress[kind])
        continue

    answer = 1

    for key in dress.keys():
        answer *= dress[key] + 1

    answer -= 1

    print(answer)
