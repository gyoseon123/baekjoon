import sys
input = sys.stdin.readline
al = {i:j for j,i in enumerate([chr(k) for k in range(ord('A'),ord('Z')+1)])}
num = {i:j for j,i in al.items()}

tree = [[0,0] for _ in range(26)]
n = int(input())
for i in range(n):
    node,left,right = input().split()
    if left != '.':
        tree[al[node]][0] = al[left]
    if right != '.':
        tree[al[node]][1] = al[right]


def preorder(v):
    left,right = tree[v][0], tree[v][1]
    print(num[v], end = '')
    if left:
        preorder(left)
    if right:
        preorder(right)


def inorder(v):
    left,right = tree[v][0], tree[v][1]
    if left:
        inorder(left)
    print(num[v], end = '')
    if right:
        inorder(right)

def postorder(v):
    left,right = tree[v][0], tree[v][1]
    if left:
        postorder(left)
    if right:
        postorder(right)
    print(num[v], end = '')

preorder(0)
print()
inorder(0)
print()
postorder(0)


