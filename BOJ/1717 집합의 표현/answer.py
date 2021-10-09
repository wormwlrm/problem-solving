import sys

input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(1_000_000)

N, M = map(int, input().split())

# 내가 지금 어디에 속해있는지
parents = {i: i for i in range(N + 1)}


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a


def find(a):
    if parents[a] == a:
        return a

    parents[a] = find(parents[a])
    return parents[a]


for _ in range(M):
    command, a, b = map(int, input().split())

    # 합집합
    if command == 0:
        union(a, b)

    # 교집합
    if command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
