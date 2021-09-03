## 2667 단지번호붙이기

<https://www.acmicpc.net/problem/2667>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- BFS 지도 탐색 문제
- child 패턴은 외워두자.

```py
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_child(dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or N <= dx or N <= dy:
        return False
    # 벽
    elif area[dy][dx] == 0:
        return False
    return True


def get_children(oy, ox):
    children = []

    for direction in directions:
        dy = direction[0] + oy
        dx = direction[1] + ox

        if is_valid_child(dy, dx):
            children.append((dy, dx))

    return children

```
