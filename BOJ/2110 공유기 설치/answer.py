import sys

input = sys.stdin.readline

N, C = map(int, input().split())

coords = []

for _ in range(N):
    coords.append(int(input()))

coords.sort()

# x: 공유기 사이의 최소 간격
# y: 설치할 수 있는 공유기 개수
left = 1
right = coords[-1] - coords[0]


def available(gap):
    count = 0
    acc = 0
    for index in range(N):
        if index == 0:
            # 0번째는 일단 넣기
            count += 1
            continue

        acc = acc + (coords[index] - coords[index - 1])

        if acc >= gap:
            acc = 0
            count += 1

    return count


answer = 0

while left <= right:
    mid = (left + right) // 2

    current = available(mid)

    # 반비례 그래프
    # 최대값 찾기이므로 왼쪽을 줄여야 함
    if current >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
