## 15649 N과 M (1)

<https://www.acmicpc.net/problem/15649>

## 내가 생각한 방법

- 백트래킹을 써야 하는데, 오랜만에 하다보니 DFS로 접근하는 방법을 까먹었다
- 1부터 N까지 반복
  - 특정 숫자를 방문함을 나타내는 `locate` 라는 재귀 함수를 둚
  - `locate`에서는 `visited`에 넣고, 길이 판단하여 early return
  - 그 후 유망한 숫자에 대해 `locate` 계속 진행
