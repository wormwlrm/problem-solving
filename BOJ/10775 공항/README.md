## 10755 공항

<https://www.acmicpc.net/problem/10775>

## 내가 생각한 방법

- 입력이 왔을 때 가장 오른쪽 게이트에서부터 채워 넣으면 된다
- 근데 이 구조를 Union Find 로 짤 수 있음
  - `P` 번째가 연결되었을 때 `P-1` 번째와 연결시킴
  - 결국 모든 게이트가 다 차게 된다면 인덱스가 0을 가리킬 것
