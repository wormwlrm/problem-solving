import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = map(str, input().strip().split())
    tree[root] = (left, right)


def preorder(root):
    left, right = tree[root]

    # 자식 없음
    if left == "." and right == ".":
        return root
    # 오른쪽만 있음
    elif left == "." and right != ".":
        return root + preorder(right)
    # 왼쪽만 있음
    elif left != "." and right == ".":
        return root + preorder(left)
    # 둘 다 있음
    else:
        return root + preorder(left) + preorder(right)


def inorder(root):
    left, right = tree[root]

    # 자식 없음
    if left == "." and right == ".":
        return root
    # 오른쪽만 있음
    elif left == "." and right != ".":
        return root + inorder(right)
    # 왼쪽만 있음
    elif left != "." and right == ".":
        return inorder(left) + root
    # 둘 다 있음
    else:
        return inorder(left) + root + inorder(right)


def postorder(root):
    left, right = tree[root]

    # 자식 없음
    if left == "." and right == ".":
        return root
    # 오른쪽만 있음
    elif left == "." and right != ".":
        return postorder(right) + root
    # 왼쪽만 있음
    elif left != "." and right == ".":
        return postorder(left) + root
    # 둘 다 있음
    else:
        return postorder(left) + postorder(right) + root


print(preorder("A"))
print(inorder("A"))
print(postorder("A"))
