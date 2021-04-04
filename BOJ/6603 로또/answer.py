from collections import deque

max_depth = 6

numbers = []
visited = deque([])
count = 0


def locate(index):
    global visited, numbers

    visited.append(numbers[index])

    if (len(visited) == max_depth):
        print(*list(visited))
        visited.pop()
    else:
        # 이제 다음 노드부터 끝까지 탐색
        for i in range(index + 1, count):
            if (promising(index, i)):
                locate(i)

        visited.pop()


def promising(index, coming):
    '''
    (index, coming) => boolean
    index: 현재 선택된 인덱스
    coming: 앞으로 선택될 인덱스

    유망성 판단하는 함수
    여기서 유망성이란 coming을 담아도 6개를 유지하는데 문제가 없는지 
    '''
    left_count = max_depth - len(visited)
    right_count = count - coming

    return left_count <= right_count


while True:
    count, *numbers = list(map(int, input().split()))

    if (count == 0):
        break

    visited = deque([])

    for i in range(count):
        locate(i)

    print('')
