## 5639 이진 검색 트리

<https://www.acmicpc.net/problem/5639>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 쉽지 않네;
- 이진트리 특) 자기보다 큰 숫자 처음 등장하면 그때부터 오른쪽 노드임
  - 자기보다 큰 숫자 없으면 오른쪽 노드 없는 것
- 만약 오른쪽 노드가 없다면
  - preorder(left) + current
- 만약 왼쪽 노드가 없다면
  - preorder(right) + current
- 둘 다 있다면
  - preorder(left) + preorder(right) + current
