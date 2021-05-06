import sys

input = sys.stdin.readline

tree_count, required = map(int, input().split())

trees = sorted(list(map(int, input().split())))

left = 0
right = trees[-1]

answer = left

while left <= right:
    mid = (left + right) // 2

    acc = 0
    for i in trees:
        acc = acc + max(i - mid, 0)
    
    if (acc >= required):
        # 너무 많이 자른 경우, 일단 가져갈 순 있기 때문에
        answer = mid
        left = mid + 1
    else:
        # 덜 잘림
        right = mid - 1


print(answer)


