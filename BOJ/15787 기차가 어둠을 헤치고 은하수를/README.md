## 15787 기차가 어둠을 헤치고 은하수를

<https://www.acmicpc.net/problem/15787>

## 내가 생각한 방법

- 비트 연산을 쓰면 된다
- 레프트 시프트 연산(`<<`)을 할 때 20번째 이상 숫자를 잘라주는 것이 필요
- 사용한 몇 가지 패턴들
  - n번째 숫자 1 만들기: `bin(binary_number | (1 << n))`
  - n번째 숫자 0 만들기: `bin(binary_number & ~(1 << n))`
  - 레프트 시프트: `bin(binary_number << n)`
  - 라이트 시프트: `bin(binary_number >> n)`
