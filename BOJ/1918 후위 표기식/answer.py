# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1918%20%ED%9B%84%EC%9C%84%20%ED%91%9C%EA%B8%B0%EC%8B%9D

import sys

input = lambda: sys.stdin.readline().rstrip()

chars = list(str(input().strip()))


def parenthese(chars):
    stack = []

    # 괄호 재귀로 처리
    for char in chars:
        # 괄호 시작일 때는 전체 스택에 담기
        if char == "(":
            stack.append(char)
        # 괄호 끝일 때는 전체 스택에서 마지막 괄호까지를 꺼내서 연산자로 만들기
        elif char == ")":
            in_parenthese = []

            while len(stack) and stack[-1] != "(":
                in_parenthese.append(stack.pop())

            # "(" 도 빼기
            stack.pop()

            # 원래 순서대로 뒤집기
            in_parenthese.reverse()

            # 괄호 안에서 다시 계산하기
            result = inorder_parser(in_parenthese)

            stack.append(result)
        # 곱셈 나눗셈 덧셈 뺄셈은 따로 처리
        else:
            stack.append(char)

    return stack


# 곱셉 나눗셈을 앞에서부터 처리
def multiply(stack):
    stack2 = []
    for char in stack:
        if len(stack2) and stack2[-1] in ["*", "/"]:
            prev = stack2.pop()
            prev2 = stack2.pop()
            stack2.append(inorder_parser([prev2, prev, char]))
        else:
            stack2.append(char)
    return stack2


# 그 후 덧셈 뺄셈을 앞에서부터 처리
def plus(stack2):
    stack3 = []
    for char in stack2:
        if len(stack3) and stack3[-1] in ["+", "-"]:
            prev = stack3.pop()
            prev2 = stack3.pop()
            stack3.append(inorder_parser([prev2, prev, char]))
        else:
            stack3.append(char)

    return stack3


def inorder_parser(chars):
    # 한 개는 바로 리턴
    if len(chars) == 1:
        return chars[0]
    # 연산자 포함 세개 오면 후위연산으로 만든 후 리턴
    elif len(chars) == 3:
        return chars[0] + chars[2] + chars[1]

    return plus(multiply(parenthese(chars)))[0]


print(inorder_parser(chars))
