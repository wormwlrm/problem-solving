import sys

input = sys.stdin.readline

count = int(input())

lines = []

for _ in range(count):
    start, end = map(int, input().split())

    lines.append((start, end))


lines.sort(key=lambda x: x[0])

# 인덱스까지 계산했을 때 나올 수 있는 가장 긴 증가부분수열의 길이
dp = [0] * 501

for i in range(count):
    # `1` ~ `x - 1`번째 값들 중,
    # x번째 값 보다 더 작은 숫자들이 갖는 부분수열의 길이 중,
    # 가장 길이가 긴 부분수열의 길이에 + 1을 한 값이,
    # x번째 값이 가지는 가장 긴 증가하는 부분 수열의 길이이다.
    dp[i] = 1
    for j in range(i + 1):
        # 현재 선택한 값이 탐색하고 있는 값보다 더 크다면
        if lines[i][1] > lines[j][1]:
            # 갱신하는데 탐색 값에 + 1 한 것 중 큰 것으로
            dp[i] = max(dp[i], dp[j] + 1)

# 최장 증가 부분 수열 길이
collect_count = max(dp)

print(count - collect_count)
