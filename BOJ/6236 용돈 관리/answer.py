import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(int(input()))

left = max(arr)
right = sum(arr)

answer = 0


def min_calc(money):
    # 총 몇 번 인출이 필요한가?
    group = 1

    remain = money
    for current in arr:
        # 현재 지출했을 때 마이너스 되는 경우
        if remain - current < 0:
            # 그룹을 늘리고 지갑 채우기
            group += 1
            remain = money - current
        else:
            remain -= current

    return group


while left <= right:
    mid = (left + right) // 2

    # min_calc는 기울기가 음수인 함수
    current = min_calc(mid)

    # 최소값을 구할 때는 오른쪽을 줄이자
    if current <= M:
        answer = mid

        # 찾는 값보다 작을 때는 오른쪽을 줄이자
        right = mid - 1
    else:
        # 찾는 값보다 클 때는 왼쪽을 늘리자
        left = mid + 1

print(answer)
