import sys

input = sys.stdin.readline

N = int(input())

maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

total_count_of_computer = 0

for i in range(N):
    for j in range(N):
        total_count_of_computer += maps[i][j]


def how_many_computers_are_cooled(height):
    acc = 0

    for i in range(N):
        for j in range(N):
            # 더 낮은 값으로 더해줌
            acc += min(height, maps[i][j])

    return acc

left = 0
right = 10000000



answer = 0
while left <= right:
    mid = (left + right) // 2

    current = how_many_computers_are_cooled(mid)

    need = total_count_of_computer / 2

    # 최소값 구하기
    # 오른쪽을 줄여야 함
    if (current >= need):
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)