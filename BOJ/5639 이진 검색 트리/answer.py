# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/5639%20%EC%9D%B4%EC%A7%84%20%EA%B2%80%EC%83%89%20%ED%8A%B8%EB%A6%AC

import sys

sys.setrecursionlimit(100_000_000)


input = lambda: sys.stdin.readline().rstrip()

order = []

while True:
    try:
        current = int(input())
        order.append(current)
    except:
        break

# 자기보다 숫자 처음 등장하는 거부터 right 임
def preorder(start, end):
    current = order[start]

    if start + 1 == end:
        return [current]

    over_index = start + 1

    while over_index < end and order[over_index] < current:
        over_index += 1

    # 오른쪽 없는 경우
    if over_index == end:
        return preorder(start + 1, over_index) + [current]

    # 왼쪽 없는 경우
    elif over_index == start + 1:
        return preorder(over_index, end) + [current]

    # 왼쪽 오른쪽 모두 있는 경우
    return preorder(start + 1, over_index) + preorder(over_index, end) + [current]


answer = preorder(0, len(order))

for i in answer:
    print(i)
