# Task2. Research about "inorder","preorder","postorder" and implement in DFS.......
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def Inorder(self, node):
        if node:
            self.Inorder(node.left)
            print(node.value, end=' ') 
            self.Inorder(node.right)

    def Preorder(self, node):
        if node:
            print(node.value, end=' ') 
            self.Preorder(node.left)
            self.Preorder(node.right)

    def Postorder(self, node):
        if node:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.value, end=' ') 

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

traversal = Tree()

print("Inorder Traversal:")
traversal.Inorder(root)
print("\n")
print("Preorder Traversal:")
traversal.Preorder(root)
print("\n")
print("Postorder Traversal:")
traversal.Postorder(root)
