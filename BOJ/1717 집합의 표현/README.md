## 1717 집합의 표현

<https://www.acmicpc.net/problem/1717>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 해시 같은 걸로 안되나? 유니온 파인드.
- 유형 자체는 떠올렸는데 시간 초과 나서 예전에 짰던 거 다시 살펴봄.
  - 유니온
    - a, b의 루트가 다르면 합침
    - `if (find[a] == find[b])`
      - `parents[a] == b`
  - 파인드
    - 자기 자신이 부모인 경우(`parents[a] == a`)는 루트임
      - `return a`
    - 중간에 자식 값을 갱신해줘야 시간 초과 안남
      - `parents[a] == find(parents[a])`
