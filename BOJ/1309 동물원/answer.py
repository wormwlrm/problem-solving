import sys

input = sys.stdin.readline

height = int(input())

divided = 9901

# 순서대로 마지막 턴까지의 00, 10, 01 갯수
share = [1, 1, 1]

for _ in range(height - 1):
    temp = []

    # 00은 00, 10, 01일 때 추가됨
    temp.append(sum(share) % divided)

    # 01은 10, 00일때 추가됨
    temp.append(sum([share[0], share[1]]) % divided)

    # 10은 01, 00일 때 추가됨
    temp.append(sum([share[0], share[2]]) % divided)

    share = temp

print(sum(share) % divided)
