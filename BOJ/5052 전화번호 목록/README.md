## 5052 전화번호 목록

<https://www.acmicpc.net/problem/5052>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 허프만 코드, 트라이(Trie) 구조를 만들어야 하는데 해시로 만들어봄
  - 딕셔너리를 하나 만들고
  - 재귀로 값을 추가함
    - ex) `911`이면 `{9: {1: 1: False}}` 이런 식
    - 마지막 값에는 `False` 를 넣어서 문자열 끝남을 알림
  - 새로 전화번호를 추가할 때 같은 레벨에 `False` 가 있다면 `NO`
  - 전화번호를 다 추가했는데 같은 레벨에서 해당 전화번호보다 더 깊은 전화번호가 있으면 `NO`
