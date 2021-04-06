import sys

gate = int(sys.stdin.readline().rstrip())
plane = int(sys.stdin.readline().rstrip())

# zero-padding
parent = [i for i in range(gate + 1)]


def find(x):
    if x == parent[x]:
        return x

    # 부모 거를 자식에 넣음
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    '''
    x와 y를 연결, 노드 숫자 작은 거를 부모로
    '''
    x_root = find(x)
    y_root = find(y)

    if (x_root == y_root):
        return

    if (x_root < y_root):
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


coming = [int(sys.stdin.readline().rstrip()) for _ in range(plane)]

answer = 0

for coming_plane in coming:
    will_dock = find(coming_plane)

    # 연결할 수 있는 0
    if (will_dock == 0):
        break

    answer += 1

    union(will_dock - 1, will_dock)

print(answer)
