# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/24087%20%E3%82%A2%E3%82%A4%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%A0%20(Ice%20Cream)

import sys
import math

input = lambda: sys.stdin.readline().rstrip()

S = int(input())
A = int(input())
B = int(input())
count = max(math.ceil((S - A) / B), 0)
print(100 * count + 250)
