#.Create a linked list containing the values 10, 20, 30, 40, 50 and display all the elements.
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
    print(temp.data, end=" ")
    temp = temp.ref