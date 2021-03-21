n = str(input())

mod = 1000000

# 제일 앞이 0으로 시작하는 문자열은 잘못된 문자열
if (n[0] == '0'):
    print(0)
else:
    # 메모이제이션을 위한 딕셔너리
    memo = {
        0: 1,
        1: 1,
    }

    # 중간에 잘못된 값 확인했을 때 탈출하기 위한 변수
    valid = True

    for i in range(1, len(n)):
        current = int(n[i - 1] + n[i])

        # 유효한 숫자 범위인지 확인,
        # 0이 포함된 거면 10, 20 외에 다른 숫자는 올 수 없음.
        if (n[i] == '0' and (current >= 30 or current == 0)):
            valid = False
            break

        # 이전 숫자가 유효한 알파벳 범위인지 확인
        elif (10 <= current <= 26):
            # 10 또는 20 일때에는 일의 자리를 따로 분리할 수 없으므로 두 번째 전의 메모이제이션을 가져옴
            if (current == 10 or current == 20):
                memo[i + 1] = memo[i - 1] % mod
            else:
                # 나머지 숫자는 일의 자리와 십의 자리를 분리하여 볼 수 있으므로 두 번째 전과 첫 번째 전의 메모이제이션을 함께 가져옴
                memo[i + 1] = (memo[i - 1] + memo[i]) % mod
        else:
            # 유효하지 않은 알파벳이면 한 개만 덧붙일 수 있다는 의미므로 첫 번째 전의 메모이제이션을 가져옴
            memo[i + 1] = memo[i] % mod

    if (valid):
        print(memo[len(n)])
    else:
        print(0)
