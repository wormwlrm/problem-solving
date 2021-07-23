import sys

input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))


dp = [[None for _ in range(N)] for _ in range(N)]


def get_value(cursor):
    return arr[cursor[0]][cursor[1]]


def get_children(cursor):
    value = get_value(cursor)

    children = []

    # 우측으로 이동 가능한 경우
    if cursor[1] + value < N:
        children.append((cursor[0], cursor[1] + value))
    # 하단으로 이동 가능한 경우
    if cursor[0] + value < N:
        children.append((cursor[0] + value, cursor[1]))

    return children


def is_answer(cursor):
    return cursor[0] == N - 1 and cursor[1] == N - 1


def bfs(cursor):
    visited = dp[cursor[0]][cursor[1]]

    # 이미 방문한 적 있으면, 그거 리턴
    if visited != None:
        return visited

    # 도착점이면 도착점까지 갈 수 있다는 의미이므로 1 리턴
    if is_answer(cursor):
        dp[cursor[0]][cursor[1]] = 1
        return 1

    # 값 0이면 같혔으므로 0 리턴
    if get_value(cursor) == 0:
        return 0

    # 도달할 수 있는 지점들을 배열로 획득
    children = get_children(cursor)

    if len(children) == 0:
        return 0
    # 다른 지점으로 bfs 시도하면서 dp에 기록함
    elif len(children) == 1:
        dp[cursor[0]][cursor[1]] = bfs(children[0])
    else:
        dp[cursor[0]][cursor[1]] = bfs(children[0]) + bfs(children[1])

    return dp[cursor[0]][cursor[1]]


print(bfs((0, 0)))
