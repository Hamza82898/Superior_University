# Task 2: BFS With Queue And Node.....
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(start):
    queue = [start]
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

print('BFS :')
bfs(root)