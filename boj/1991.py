N = int(input())

graph = {}
for _ in range(N):
    root, left, right = input().split()
    graph[root] = (left, right)


def preorder_traverse(node):
    if node == ".":
        return
    print(node, end="")
    preorder_traverse(graph[node][0])
    preorder_traverse(graph[node][1])


def inorder_traverse(node):
    if node == ".":
        return
    inorder_traverse(graph[node][0])
    print(node, end="")
    inorder_traverse(graph[node][1])


def postorder_traverse(node):
    if node == ".":
        return
    postorder_traverse(graph[node][0])
    postorder_traverse(graph[node][1])
    print(node, end="")


preorder_traverse("A")
print()
inorder_traverse("A")
print()
postorder_traverse("A")