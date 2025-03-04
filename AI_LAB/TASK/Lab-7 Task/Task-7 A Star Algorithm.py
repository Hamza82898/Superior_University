# Task 7- A-Star Algorithm...

graph = {
    'A' : {'B' : 1, 'C' : 3},
    'B' : {"D" : 3},
    'C' : {'D' : 2},
    'D' : {}
}

h_cost = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 0
}

def A_star(start, goal):
    list = [start]
    g_cost = {start: 0}
    parent = {start: None}

    while list:
        current = min(list, key=lambda node: g_cost[node] + h_cost[node])
        if current == goal:
            return reconstruct_path(parent, goal)
        list.remove(current)

        for neighbour in graph[current]:
            new_g_cost = g_cost[current] + graph[current][neighbour]

            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost
                parent[neighbour] = current
                if neighbour not in list:
                    list.append(neighbour)

    return None

def reconstruct_path(parent, node):
    path = []
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1]

path = A_star('A', 'D')
if path:
    print("Path Found:", " -> ".join(path))
else:
    print("No Path Found!")                        