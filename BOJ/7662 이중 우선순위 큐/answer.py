import sys
import heapq

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    k = int(input())

    # 오름차순, 작은 게 앞
    min_heap = []
    # 내림차순, 음수 붙여서 큰 게 앞에
    max_heap = []

    count = {}

    for i in range(k):
        command, num = map(str, input().split())
        num = int(num)

        # 숫자 더하기
        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)

            if num not in count:
                count[num] = 0
            count[num] += 1

        elif command == "D":
            # 든 거 없으면 패스
            if len(min_heap) == 0:
                continue

            # 최대값 삭제
            elif num == 1:
                while max_heap:
                    maximum = -heapq.heappop(max_heap)

                    # 카운트가 있는 것만 실제 갯수로 반영, 나머지는 날림
                    if (maximum in count) and count[maximum] > 0:
                        count[maximum] -= 1

                        if count[maximum] == 0:
                            del count[maximum]

                        break

            # 최소값 삭제
            elif num == -1:
                while min_heap:
                    minimum = heapq.heappop(min_heap)

                    # 카운트가 있는 것만 실제 갯수로 반영, 나머지는 날림
                    if (minimum in count) and count[minimum] > 0:
                        count[minimum] -= 1

                        if count[minimum] == 0:
                            del count[minimum]

                        break

    if count:
        sorted_items = sorted(count.items())
        print(sorted_items[-1][0], sorted_items[0][0])
    else:
        print("EMPTY")
