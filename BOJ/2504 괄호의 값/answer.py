import sys
from collections import deque
import re

input = sys.stdin.readline


string = str(input().rstrip())


def is_valid(string):
    stack = deque([])

    try:
        for current in list(string):
            if current == ")":
                last = stack.pop()
                if last == "(":
                    continue
                else:
                    return False
            elif current == "]":
                last = stack.pop()
                if last == "[":
                    continue
                else:
                    return False
            else:
                stack.append(current)
    except:
        return False

    return len(stack) == 0


if not is_valid(string):
    print(0)
else:
    arr = list(string)
    while len(arr) > 1:
        temp = arr[::]
        for index in range(len(arr) - 1):
            current = arr[index]

            # 다음값 설정
            if index < len(arr) - 1:
                next = arr[index + 1]
            else:
                next = None

            # 다음값2 설정
            if index < len(arr) - 2:
                next_2 = arr[index + 2]
            else:
                next_2 = None

            # '[', ']' => 3으로 치환
            if current == "[" and next == "]":
                temp = temp[:index:] + [3] + temp[index + 2 : :]
                break
            # '(', ')' => 2로 치환
            elif current == "(" and next == ")":
                temp = temp[:index:] + [2] + temp[index + 2 : :]
                break
            # 연속한 숫자 => 합으로 치환
            elif type(current) == int and type(next) == int:
                acc = current + next
                temp = temp[:index:] + [acc] + temp[index + 2 : :]
                break
            # '(', 숫자, ')' => 2 곱한 수로 치환
            elif current == "(" and type(next) == int and next_2 == ")":
                multiply = next * 2
                temp = temp[:index:] + [multiply] + temp[index + 3 : :]
                break
            # '[', 숫자, ']' => 3 곱한 수로 치환
            elif current == "[" and type(next) == int and next_2 == "]":
                multiply = next * 3
                temp = temp[:index:] + [multiply] + temp[index + 3 : :]
                break

        arr = temp

    print(arr[0])
