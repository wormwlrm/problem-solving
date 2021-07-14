import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())

cakes = list(map(int, input().split()))

queue = PriorityQueue()

for cake in cakes:
    if cake % 10 == 0:
        queue.put((-1000 / cake, cake))
    else:
        queue.put((cake, cake))

answer = 0

cut = M
while cut > 0 and not queue.empty():
    current = queue.get()

    # 길이 10짜리는 그냥 꺼내기
    if current[1] == 10:
        answer += 1
    # 길이 20짜리는 커트 하고 2개 꺼내기
    elif current[1] == 20:
        answer += 2
        cut -= 1
    # 10보다 작으면 버리기
    elif current[1] < 10:
        continue
    # 10보다 크면 10으로 한 번 커트하고 큐에 다시 집어넣음
    elif 10 < current[1]:
        answer += 1
        cut -= 1
        queue.put((current[0], current[1] - 10))

print(answer)
