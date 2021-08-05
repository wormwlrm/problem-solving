import sys

input = sys.stdin.readline

N, D, K, C = map(int, input().split())

table = []

for _ in range(N):
    table.append(int(input()))

window_dishes = [0] * (D + 1)

# 쿠폰은 일단 먹고 시작
window_dishes[C] = 1
window_sum = 1

total = 1

# 처음 토탈 초기화
for index in table[0:K:]:
    # 한 번도 안 먹은 거면 토탈 + 1
    if window_dishes[index] == 0:
        window_sum += 1
        total += 1
    window_dishes[index] += 1

for i in range(N):
    left_index = table[i % N]
    # 왼쪽 한 칸 뺌
    window_dishes[left_index] -= 1
    # 안 먹은 걸로 되면 토탈 - 1
    if window_dishes[left_index] == 0:
        window_sum -= 1

    right_index = table[(i + K) % N]
    # 오른쪽 한 칸 더함
    window_dishes[right_index] += 1
    # 한 번도 안 먹은 거면 토탈 + 1
    if window_dishes[right_index] == 1:
        window_sum += 1

    total = max(total, window_sum)

print(total)
