# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/11058%20%ED%81%AC%EB%A6%AC%EB%B3%B4%EB%93%9C

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 기본적으로 하나씩 입력한다고 가정했을 때
dp = list(range(101))

depth = 0

# 전체 선택 / 복사 / 붙여넣기까지 걸리는 시간이 3턴임
index = 4

while index < 101:
    addictive = dp[index - 3]

    count = 1

    for i in range(index, 101):
        dp[i] = max(dp[i], addictive + addictive * count)
        count += 1

    index += 1

print(dp[N])
