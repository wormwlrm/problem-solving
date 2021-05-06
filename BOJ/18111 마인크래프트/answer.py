import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

maps = []

min_height = 256
max_height = 0

for i in range(N):
    line = list(map(int, input().split()))
    min_height = min(*line, min_height)
    max_height = max(*line, max_height)
    maps.append(line)

min_cost = float("inf")
height = 0


for i in range(min_height, max_height + 1):
    current_cost = 0
    remain_block = B

    # 타겟으로 하는 거보다 높은거를 먼저 깎아서 블록 확보해야 함
    for j in maps:
        for k in j:
            if (k > i):
                # 깎아야 한다
                current_cost += (k - i) * 2
                remain_block += (k - i)

    # 그 후 타겟으로 하는 거보다 낮은 거 메꾸기
    for j in maps:
        for k in j:
            if (k < i):
                # 일단 설치해봄
                remain_block -= (i - k)
                current_cost += (i - k)
                
                # 블록이 음수가 되면 안됨.
                if (remain_block < 0):
                    current_cost = float("inf")
                    break
    
    # 땅의 높이가 가장 높은 것을 출력할 것이니까 같더라도 갱신함
    if (current_cost <= min_cost):
        min_cost = current_cost
        height = i

print(min_cost, height)