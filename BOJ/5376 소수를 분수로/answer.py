import sys
from math import gcd

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = str(input().rstrip())

    # 순환 소수는 따로 처리
    if num.count("(") or num.count(")"):
        # 순환 소수 시작 전에 몇 째 자리 있는지 확인
        infinite_start = num.index("(")
        infinite_end = num.index(")")

        before_number = num[2:infinite_start:]
        loop_number = num[infinite_start + 1 : infinite_end :]

        if len(before_number):
            ja = int(before_number + loop_number) - int(before_number)
        else:
            ja = int(loop_number)

        mo = "9" * (len(before_number) + len(loop_number))
        if len(before_number):
            mo = mo[: len(mo) - len(before_number) :] + "0" * len(before_number)

        mo = int(mo)
    else:
        # 소숫점 뒷자리부터 몇 개 자리의 숫자 오는지
        ja = int(num[2::])
        mo = 10 ** (len(num[2::]))

    divider = gcd(mo, ja)
    print(str(ja // divider) + "/" + str(mo // divider))
