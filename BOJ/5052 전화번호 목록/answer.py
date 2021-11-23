# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/5052%20%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8%20%EB%AA%A9%EB%A1%9D

import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())

    phone_book = {}

    answer = True

    for i in range(N):
        phone_number = list(map(int, list(input())))

        current_page = phone_book

        try:
            for number in phone_number:
                for key in current_page.keys():
                    if current_page[key] == False:
                        answer = False
                        break

                if number not in current_page:
                    current_page[number] = {}

                current_page = current_page[number]

            if number in current_page:
                raise

            current_page[number] = False
        except:
            answer = False
            break

    print("YES" if answer else "NO")
