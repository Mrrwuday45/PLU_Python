graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

v1 = input("enter first Vertex: ")
v2 = input("enter second Vertex: ")

if v2 in graph[v1]:
    print("edge Exists")
else:
    print("edge Does Not Exist")