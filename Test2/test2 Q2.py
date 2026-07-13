#Insert a new node containing 25 after the node containing 20.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

values = [10, 20, 30, 40, 50]

head = Node(values[0])
temp = head

for i in range(1, len(values)):
    new_node = Node(values[i])
    temp.ref = new_node
    temp = new_node

temp = head

while temp != None:
    if temp.data == 20:
        new_node = Node(25)
        new_node.ref = temp.ref
        temp.ref = new_node
        break
    temp = temp.ref

temp = head

while temp != None:
    print(temp.data, end=" ")
    temp = temp.ref