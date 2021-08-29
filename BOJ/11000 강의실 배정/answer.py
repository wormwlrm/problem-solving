import sys
import heapq

input = sys.stdin.readline

N = int(input())

schedules = []

rooms = []

for _ in range(N):
    start, end = map(int, input().split())

    schedules.append((start, end))


schedules.sort(key=lambda x: (x[0], x[1]))

rooms.append(schedules[0][1])

for index in range(1, N):
    start, end = schedules[index]

    # 종료 시각보다 새 회의가 늦게 열리면, 회의실 추가로 만들 필요 없음.
    if rooms[0] <= start:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    # 일찍 열린다면 회의실을 추가로 만듦
    else:
        heapq.heappush(rooms, end)


print(len(rooms))
