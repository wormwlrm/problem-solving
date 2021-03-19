import sys
ipt = sys.stdin.readline

arr = set()

for i in range(int(ipt())):
    arr.add(int(ipt()))


arr = sorted(arr)

for i in list(arr):
    print(i)
