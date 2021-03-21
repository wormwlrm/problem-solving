n = int(input())

n_cards = list(map(int, input().split()))

dic = {}

for i in n_cards:
    if (i not in dic):
        dic[i] = 0
    dic[i] += 1

k = int(input())

k_cards = list(map(int, input().split()))

answer = []

for k in k_cards:
    if (k not in dic):
        answer.append(0)
    else:
        answer.append(dic[k])

print(' '.join(map(str, answer)))
