import sys
import math

input = sys.stdin.readline

N = int(input())

Q, *M = map(int, input().split())

dp = [1, 1]

# dp로 일단 팩토리얼 구하자
for i in range(2, 21):
    dp.append(i * dp[-1])

# target번째 숫자 구하기
if Q == 1:
    # 목표 인덱스
    target = M[0]

    # 현재 단계
    current = N - 1

    # 사용한 숫자 저장
    numbers = [i for i in range(1, N + 1)]

    # 정답 배열
    answer = []

    # 누적값
    acc = 0

    while numbers:
        nth = math.ceil((target - acc) / dp[current])

        answer.append(numbers[nth - 1])
        numbers.remove(numbers[nth - 1])

        acc += (nth - 1) * dp[current]
        current -= 1

    print(*answer)


# M이 몇 번째 인덱스인지 구하기
else:
    # 찾고자 하는 숫자
    targets = M[::]

    # 현재 단계
    current = N - 1

    # 사용한 숫자 저장
    numbers = [i for i in range(1, N + 1)]

    # 정답
    left = dp[1]
    right = dp[-1]

    # 누적값
    acc = 0

    for target in targets:
        nth = numbers.index(target)

        left = acc + (nth * dp[current] + 1)
        right = acc + ((nth + 1) * dp[current])

        numbers.remove(numbers[nth])

        acc += (nth) * dp[current]
        current -= 1

    print(left)
