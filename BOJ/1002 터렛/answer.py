import sys
import math

input = sys.stdin.readline

count = int(input())

for _ in range(count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 중심이 같은 경우
    if distance == 0:
        # 반지름이 같은 경우 (8)
        if r1 == r2:
            print(-1)
        # 반지름 다른 경우(7)
        else:
            print(0)
    # 겹치는 경우(3)
    # 겹치는 경우(5)
    elif abs(r2 - r1) < distance < r1 + r2:
        print(2)
    # 외접하는 경우(2)
    # 내접하는 경우(4)
    elif r1 + r2 == distance or abs(r2 - r1) == distance:
        print(1)
    # 아예 안 닿는 경우(1)
    else:
        print(0)
