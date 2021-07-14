import sys

input = sys.stdin.readline

poll_count = int(input())

polls = [0] * 1001

heights = set([])

# 기둥이 박혀있는 가장 왼쪽 인덱스
min_left_index = 1001
# 기둥이 박혀있는 가장 오른쪽 인덱스
max_right_index = 0

for i in range(poll_count):
    L, H = map(int, input().split())

    min_left_index = min(min_left_index, L)
    max_right_index = max(max_right_index, L)

    polls[L] = H
    heights.add(H)

heights = sorted(heights, reverse=True)

visited_left = None
visited_right = None

# 일단 가능한 모든 높이에 대해 반복을 실행해보자
for height in heights:
    # 왼쪽부터 방문했을 때 height를 넘기는 첫 번째 기둥의 인덱스
    for index in range(min_left_index, max_right_index):
        if polls[index] >= height:
            temp_left = index
            break

    # 오른쪽부터 방문했을 때 height를 넘기는 첫 번째 기둥의 인덱스
    for index in range(min_left_index, max_right_index):
        if polls[1000 - index] >= height:
            temp_right = 1000 - index
            break

    # 처음에 한해서 같은 높이의 기둥 사이를 가득 채워줌
    if visited_left == None:
        visited_left = temp_left
        visited_right = temp_right
        for j in range(visited_left, visited_right + 1):
            polls[j] = height

    # 이미 방문한 왼쪽보다 더 왼쪽에서 새로운 인덱스가 발견되었다면
    if temp_left < visited_left:
        # 해당 범위 내의 기둥 높이를 height로 조정함
        for j in range(temp_left, visited_left):
            polls[j] = height
        visited_left = temp_left

    # 이미 방문한 오른쪽보다 더 오른쪽에서 새로운 인덱스가 발견되었다면
    if visited_right < temp_right:
        # 해당 범위 내의 기둥 높이를 height로 조정함
        for j in range(visited_right + 1, temp_right + 1):
            polls[j] = height
        visited_right = temp_right

print(sum(polls))
