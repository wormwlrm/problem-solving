import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    members = []

    for _ in range(N):
        L, R = map(int, input().split())
        members.append((L, R))

    members.sort(key=lambda x: (x[0], x[1]))

    choose = [True] * N

    L_min = members[0]
    R_min = members[0]

    for i in range(1, N):
        # 현재 왼쪽, 오른쪽 점수 구함
        CL, CR = current = members[i]

        # 현재 왼쪽 점수가 더 낮으면 갱신, 빠질 녀석으로 선택하지 않기
        if CL < L_min[0]:
            L_min = current
            continue

        # 현재 오른쪽 점수가 더 낮으면 갱신, 빠질 녀석으로 선택하지 않기
        elif CR < R_min[1]:
            R_min = current
            continue

        # 아무것도 없다면 위험함
        choose[i] = False

    print(choose.count(True))
