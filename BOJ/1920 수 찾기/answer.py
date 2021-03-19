n = int(input())

dict_n = {}

a = list(map(int, input().split()))

for i in a:
    dict_n[i] = True

n = int(input())

b = list(map(int, input().split()))

for i in b:
    if (i in dict_n):
        print(1)
    else:
        print(0)
