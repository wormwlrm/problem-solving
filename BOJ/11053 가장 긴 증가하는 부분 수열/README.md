## 11053 가장 긴 증가하는 부분 수열

<https://www.acmicpc.net/problem/11053>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- LIS를 해보자.
  - 최장 증가 부분 수열
- N에 대해서
  - N 앞에 있는 숫자들 중, 현재 숫자보다 큰 값의 DP값 가져옴
  - 해당 값 + 1 을 DP에 저장
