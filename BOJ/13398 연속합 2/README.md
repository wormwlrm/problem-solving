## 13398 연속합 2

<https://www.acmicpc.net/problem/13398>

## 내가 생각한 방법

![이미지](./img.png)

- DP로 풂
- dp1은 연속된 숫자를 고르는 경우, N번째까지 고른 경우에서 가장 큰 값
  - dp_1[i - 1] + numbers[i]: 이전까지의 누적값 + 현재값
  - numbers[i]: 단순 현재값, 위 값이 음수일 수 있기 때문
- dp2는 숫자 1개를 뺀 경우
  - dp_1[i - 2] + numbers[i]: i-2번째까지의 최대값 + 현재값, 즉 i-1번째를 뺀 거
  - dp_2[-1] + numbers[i]: 이전에 i-1번째가 제거된 값 + 현재값, 즉 i-N번째가 빠진 값
- 근데 다른 사람 풀이가 더 나은 듯 하다.
  - <https://kyun2da.github.io/2020/09/22/sequenceSum/>
