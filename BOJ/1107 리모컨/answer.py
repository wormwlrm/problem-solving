import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

M = int(input())

init = 100

numbers = list(range(10))

if M > 0:
    for number in list(map(int, input().split())):
        numbers.remove(number)


def is_matched(num: int):
    return set(list(map(int, list(str(num))))).issubset(set(numbers))


def all_blocked():
    return len(numbers) == 0


def only_zero():
    return len(numbers) == 1 and numbers[0] == 0


def get_answer():
    # N이 매칭될 경우
    if N == init:
        return 0

    if is_matched(N):
        return min(len(str(N)), abs(init - N))

    if all_blocked():
        return abs(N - init)

    # 0 누르고 처음부터 올라가기, init에서 깎아가기
    if only_zero():
        return min(abs(N + 1), abs(init - N))

    # upper 구하기
    upper_value = N
    upper_counter = 1

    while True:
        if is_matched(N + upper_counter):
            upper_value = N + upper_counter
            break
        upper_counter += 1

    upper = min(len(str(upper_value)) + upper_counter, abs(init - N))

    # bound 구하기
    bound_value = N
    bound_counter = 1

    while N - bound_counter >= 0:
        if is_matched(N - bound_counter):
            bound_value = N - bound_counter
            break
        bound_counter += 1

    # bound 에서 찾은 경우
    if bound_value != N:
        bound = min(len(str(bound_value)) + bound_counter, abs(init - N))
    # bound에서 못 찾은 경우
    else:
        # bound가 0인 경우,
        if 0 in numbers:
            bound = 1
        else:
            bound = float("inf")

    return min(upper, bound)


print(get_answer())
