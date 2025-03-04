# Task 1: BFS without Queue And Nodes.
def bfs(graph, current):
    if not current:
        return
    
    for node in current:
        print(node, end=" ")
    next_level = []
    for node in current:
        next_level.extend(graph.get(node, []))
    bfs(graph, next_level)

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}            
print("BFS :")
bfs(graph, ['B'])