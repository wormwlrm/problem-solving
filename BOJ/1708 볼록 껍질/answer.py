import sys
from collections import deque
from functools import cmp_to_key

input = sys.stdin.readline

N = int(input())


class Point:
    def __init__(self, x=0, y=0, rx=0, ry=0) -> None:
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        pass


points = []


for i in range(N):
    x, y = map(int, input().split())

    points.append(Point(x, y))

# 점 A,B,C 를 순서대로 봤을 때 시계 방향인지 반시계 방향인지를 구함
# 벡터 AB, AC의 외적
# > 0: 반시계
# = 0: 평행
# < 0: 시계
def ccw(A: Point, B: Point, C: Point):
    return (B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y)


# 반시계 순 정렬
def compare(A, B):
    angle = ccw(orientation, A, B)

    # 각도 작은 순
    # ccw 음수일수록 앞에 오게
    if angle != 0:
        return -angle

    # 일직선일 경우 좌표 작은 순서대로
    if A.x == B.x:
        return A.y - B.y
    if A.y == B.y:
        return A.x - B.x
    else:
        return A.rx ** 2 + A.ry ** 2 - B.rx ** 2 - B.ry ** 2


# y, x 순으로 정렬, 0번이 제일 왼쪽에 오게
points.sort(key=lambda p: (p.y, p.x))

# 원점
orientation, *points = points

# 상대 좌표
for i in range(N - 1):
    points[i].rx = points[i].x - orientation.x
    points[i].ry = points[i].y - orientation.y


points = [orientation] + sorted(points, key=cmp_to_key(compare))


stack = deque([])
stack.append(points[0])
stack.append(points[1])

for i in range(2, N):
    current = points[i]

    while len(stack) >= 2:
        second = stack.pop()
        first = stack[len(stack) - 1]

        # 탈출 조건, 반시계 방향이라면 탈출
        if ccw(first, second, current) > 0:
            stack.append(second)
            break

    stack.append(points[i])

print(len(stack))
