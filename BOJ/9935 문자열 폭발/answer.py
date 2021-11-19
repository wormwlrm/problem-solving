# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/9935%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%ED%8F%AD%EB%B0%9C

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

stack = []

string = list(str(input()))

bomb = str(input())


def is_bomb_in():
    if len(stack) < len(bomb):
        return False

    if "".join(stack[-len(bomb) : :]) == bomb:
        return True

    return False


def boom():
    count = 0
    while count < len(bomb):
        stack.pop()
        count += 1


for char in string:
    stack.append(char)

    while is_bomb_in():
        boom()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
