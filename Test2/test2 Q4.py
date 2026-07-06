class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

def count(head):
    c = 0
    temp = head
    while temp != None:
        c += 1
        temp = temp.ref
    return c

values = [10, 20, 30, 40, 50]

head = Node(values[0])
temp = head
for i in range(1, len(values)):
    new_node = Node(values[i])
    temp.ref = new_node
    temp = new_node

print("Number of nodes in the linked list:", count(head))   
