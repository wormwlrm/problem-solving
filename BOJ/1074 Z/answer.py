import sys

sys.setrecursionlimit(15000)

input = sys.stdin.readline

N, target_r, target_c = map(int, input().split())

width = 2 ** N

counter = 0


def z_traversal(width, l, t, r, b):
    global counter

    # 좌상단에 있는 경우
    if target_r < t + width / 2 and target_c < l + width / 2:
        if width == 2:
            return counter

        # 카운터는 건들지 않음
        return z_traversal(width // 2, l, t, r // 2, b // 2)

    # 우상단
    if target_r < t + width / 2 and target_c >= l + width / 2:
        if width == 2:
            return counter + 1

        # 카운터 더해줌
        counter += (width // 2) ** 2 * 1

        return z_traversal(width // 2, l + width // 2, t, r, b // 2)

    # 좌하단
    if target_r >= t + width / 2 and target_c < l + width / 2:
        if width == 2:
            return counter + 2

        # 카운터 더해줌
        counter += (width // 2) ** 2 * 2
        return z_traversal(width // 2, l, t + width // 2, r // 2, b)

    # 우하단
    if target_r >= t + width / 2 and target_c >= l + width / 2:
        if width == 2:
            return counter + 3

        # 카운터 더해줌
        counter += (width // 2) ** 2 * 3
        return z_traversal(width // 2, l + width // 2, t + width // 2, r, b)


print(z_traversal(width, 0, 0, width - 1, width - 1))
