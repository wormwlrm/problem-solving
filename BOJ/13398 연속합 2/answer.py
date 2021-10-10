import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

numbers = list(map(int, input().split()))


# zero padding, 나중에 잘라냄
dp_1 = [numbers[0]]

for i in range(1, N):
    maximum = max(dp_1[i - 1] + numbers[i], numbers[i])
    dp_1.append(maximum)

# zero padding, 나중에 잘라냄
dp_2 = [dp_1[0]]

# 3개부터 의미 있음
if len(numbers) > 2:
    for i in range(2, len(numbers)):
        # i - 1 번째를 뺌
        maximum = max(dp_1[i - 2] + numbers[i], dp_2[-1] + numbers[i])
        dp_2.append(maximum)


print(max(dp_1 + dp_2))
