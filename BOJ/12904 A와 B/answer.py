# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/12904%20A%EC%99%80%20B

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

start = input()

end = input()


def cut(start: str, end: str):
    if len(start) > len(end):
        return False

    index = len(end) - 1

    while len(start) < len(end):
        # A면 그냥 깎기
        if end[index] == "A":
            end = end[:index:]
        elif end[index] == "B":
            end = end[:index:]
            end = end[::-1]
        index -= 1

    if start == end:
        return 1
    return 0


print(cut(start, end))
