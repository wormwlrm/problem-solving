## 2869 달팽이는 올라가고 싶다

<https://www.acmicpc.net/problem/2869>

## 내가 생각한 방법

- N일동안 올라갈 수 있는 높이는 `(up - down) * (day - 1) + up`
- 위 값이 `height` 보다 커질 때를 찾으면 된다
- 부등식으로 나타내면 `ceil((height - up) / (up - down)) + 1`
