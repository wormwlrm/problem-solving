## 11501 주식

<https://www.acmicpc.net/problem/11501>

## 내가 생각한 방법

- 처음에 `max` 값을 갱신해두고, 그것보다 작으면 사고 같으면 파는 방식으로 짬
  - 하지만 시간 초과 발생
  - 주식을 팔 때마다 나머지 값에 대해 `max` 를 갱신해주어야 하기 때문
- 뒤에서부터 접근하면 `max`를 계산해 둘 필요가 없음
  - 현재값보다 작은 값은 무조건 팔고, 큰 값이면 갱신하면 됨
  - 따라서 O(n) 이면 끝
