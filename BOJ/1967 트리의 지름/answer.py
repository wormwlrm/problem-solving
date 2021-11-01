# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1967%20%ED%8A%B8%EB%A6%AC%EC%9D%98%20%EC%A7%80%EB%A6%84

import sys

sys.setrecursionlimit(10 ** 9)

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

parents = {i: -1 for i in range(1, N + 1)}

children = {i: [] for i in range(1, N + 1)}

# zero padding
weights = {i: {} for i in range(0, N + 1)}

weights[0][1] = 0


for _ in range(N - 1):
    # 부모 자식 가중치
    parent, child, weight = map(int, input().split())

    # 자식에게 부모 붙이기
    parents[child] = parent

    # 부모에게 자식 붙이기
    children[parent].append(child)

    weights[parent][child] = weight

maximum = -1


def recursive(prev, current):
    global maximum, weights

    # 자식이 없으면 가중치 값만 리턴
    if len(children[current]) == 0:
        maximum = max(maximum, weights[prev][current])
        return weights[prev][current]

    # 자식을 방문하면서 나올 수 있는 가중치 값을 모두 계산
    acc = []

    for child in children[current]:
        acc.append(recursive(current, child))

    # 큰 순서대로 정렬
    acc.sort(reverse=True)

    # 트리의 자식 여러개인 경우
    if len(acc) > 1:
        # 부모 + 제일 큰 자식 vs 자식 중 제일 큰 거 두 개
        maximum = max(maximum, weights[prev][current] + acc[0], acc[0] + acc[1])

    # 자식 한개인 경우
    else:
        # 부모 + 자식
        maximum = max(maximum, weights[prev][current] + acc[0])

    # 리턴하는 값은 부모와 연결되어야 하므로, 부모의 가중치 + 가장 큰 자식의 가중치
    return weights[prev][current] + acc[0]


recursive(0, 1)

print(maximum)
