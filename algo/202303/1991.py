# 1991 트리 순회 (2023/03/24)
from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
graph = [[-1, -1] for _ in range(26)]
for _ in range(N):
    parent, left, right = map(str, input().split())
    if left != '.':
        graph[ord(parent) - 65][0] = (ord(left) - 65)
    if right != '.':
        graph[ord(parent) - 65][1] = (ord(right) - 65)

def preorder(root):
    if root != -1:
        print(chr(root+65), end='')
        preorder(graph[root][0])
        preorder(graph[root][1])

def inorder(root):
    if root != -1:
        inorder(graph[root][0])
        print(chr(root+65), end='')
        inorder(graph[root][1])

def postorder(root):
    if root != -1:
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(chr(root+65), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)