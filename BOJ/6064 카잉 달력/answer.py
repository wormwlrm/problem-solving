import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    M, N, x, y = map(int, input().split())

    answer = -1

    dic = {}

    count = 0

    # x 초기화
    while True:
        current = count * M + x
        if current > M * N:
            break

        dic[current] = True
        count += 1

    count = 0

    current = y

    # y 초기화
    while current <= N * M:
        current = count * N + y

        if current in dic:
            answer = current
            break
        count += 1

    print(answer)
