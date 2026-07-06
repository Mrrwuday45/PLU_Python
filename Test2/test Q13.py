class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("root =", root.data)
print("left Child =", root.left.data)
print("right Child =", root.right.data)