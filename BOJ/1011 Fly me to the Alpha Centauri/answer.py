# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1011%20Fly%20me%20to%20the%20Alpha%20Centauri

import sys
import math

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    answer = 0
    distance = y - x

    # 배열의 총 합
    value = math.floor(math.sqrt(distance))

    # 합의 2배 - 1은 일단 초기값
    answer += value * 2 - 1

    # 남은 거
    remain = distance - value ** 2

    # 남은 거 있으면 자리수 더해주기
    if remain != 0:
        if remain <= value:
            answer += 1
        else:
            answer += 2

    print(answer)
