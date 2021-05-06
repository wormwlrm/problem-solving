import sys
import math
from collections import Counter 

input = sys.stdin.readline

count = int(input())

arr = []
for i in range(count):
    arr.append(int(input()))
arr.sort()

# 평균
print(int(round(sum(arr) / count)))

# 중앙값
print(arr[count // 2])

# 최빈값
cnt = Counter(arr)
temp = cnt.most_common(2)

if (len(temp) == 1):
    print(temp[0][0])
elif (temp[0][1] == temp[1][1]):
    print(temp[1][0])
else:
    print(temp[0][0])

# 범위
print(arr[-1] - arr[0])
