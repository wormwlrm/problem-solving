n = int(input())

n_cards = list(map(int, input().split()))

dic = {}

for i in range(n_cards):
    if (i not in dic):
        dic[i] = 0
    dic[i] += 1

k = int(input())

k_cards = list(map(int, input().split()))

for k in range(k_cards):
    if (k not in dic):
        print(0, end=" ")
    else:
        print(dic[i], end=" ")
