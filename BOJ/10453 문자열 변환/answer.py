import sys

input = sys.stdin.readline

count = int(input())

for i in range(count):
    s1, s2 = map(str, input().rstrip().split())

    cursor1 = 0
    cursor2 = 0

    answer = 0

    while not (cursor1 == len(s1) and cursor2 == len(s2)):
        # 커서값 같을때는 통과
        if s1[cursor1] == s2[cursor2]:
            # b 일때만 값 누적
            if s1[cursor1] == "b":
                answer += abs(cursor2 - cursor1)
            cursor1 += 1
            cursor2 += 1
        # a 인것만 올려줌. 우리는 b 갯수만 맞추면 됨.
        elif s1[cursor1] == "a":
            cursor1 += 1
        elif s2[cursor2] == "a":
            cursor2 += 1

    print(answer)
