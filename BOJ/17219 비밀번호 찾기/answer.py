import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dic = {}

for i in range(N):
    id, pw = map(str, input().rstrip().split())

    dic[id] = pw

for i in range(M):
    id = input().rstrip()
    print(dic[id])
