count = int(input())

mans = []

for i in range(count):
    x, y = map(int, input().split())
    mans.append((x, y))

answer = []

for i in range(len(mans)):
    rank = 1

    for j in range(len(mans)):
        # 자기 자신과 비교는 제외
        if (i == j):
            continue
        
        # 나보다 큰 사람만 확인하면 됨
        if (mans[i][0] < mans[j][0]) and (mans[i][1] < mans[j][1]):
            rank += 1

    answer.append(rank)

print(*answer, sep=" ", end="")