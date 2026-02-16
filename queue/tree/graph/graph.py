graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print("Graph connections:")
for node in graph:
    print(node, "->", graph[node])
