# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1339%20%EB%8B%A8%EC%96%B4%20%EC%88%98%ED%95%99

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

points = {}

strings = []

for _ in range(N):
    char = input()

    digit = len(char) - 1

    for i in list(char):
        if i not in points:
            points[i] = 0
        points[i] += 9 * (10 ** digit)
        digit -= 1

    strings.append(char)

points = dict(sorted(points.items(), key=lambda x: x[1], reverse=True))

mapping = {value: 9 - index for index, value in enumerate(points.keys())}


def convert_string_to_number(string):
    result = 0
    digit = len(string) - 1
    for i in list(string):
        result += mapping[i] * (10 ** digit)
        digit -= 1
    return result


numbers = list(map(convert_string_to_number, strings))

print(sum(numbers))
