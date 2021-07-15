import sys

input = sys.stdin.readline

max_len = int(input().rstrip())

candidate_count = int(input().rstrip())

candidates = list(map(int, input().split()))

current_winners = {}

# zero padding, 최대 100명 학생
points = [0] * 101

for index, candidate in enumerate(candidates):
    # 이미 등록된 후보의 경우에는 포인트만 증가
    if candidate in current_winners:
        points[candidate] += 1

    # 액자 가득 안 찬 경우, 처음에 한해 시간 기록하고 포인트 증가
    elif len(current_winners.keys()) < max_len:
        if candidate not in current_winners:
            current_winners[candidate] = index
        points[candidate] += 1

    # 액자가 새 후보가 등록되어야 하는 경우
    else:
        # 이름, 득표, 등록된 순서
        min_winner = (0, float("inf"), float("inf"))

        for winner in current_winners.keys():
            # 추천 횟수 제일 작은 사람 찾기
            if points[winner] < min_winner[1]:
                min_winner = (winner, points[winner], current_winners[winner])
            # 혹시 추천 횟수 같은 사람 있으면, 제일 오래전에 등록된 사람을 선택
            elif points[winner] == min_winner[1]:
                if current_winners[winner] < min_winner[2]:
                    min_winner = (winner, points[winner], current_winners[winner])

        name = min_winner[0]

        points[name] = 0
        del current_winners[name]

        current_winners[candidate] = index
        points[candidate] += 1


print(*sorted(list(current_winners.keys())))
