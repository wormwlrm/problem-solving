## 21600 계단

<https://www.acmicpc.net/problem/21600>

## 내가 생각한 방법

![이미지](./img.png)

- DP의 향기가 느껴진다
- 뭐지? 너무 쉽게 품
  - 점화식은 `dp[index] = min(dp[index - 1] + 1, steps[index])`
  - 이전 DP에서 1 더한 거랑 히스토그램 최대 높이 중 작은 거 선택하면 됨
