# Task 1..... DFS With Stack And Node......
tree = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = list()
stack = []

def dfs(start, goal):
    if start not in visited:
        visited.append(start)
        stack.append(start)
        print(f"Visited : {start}")
        print()

        if start == goal:
            print(f"This is {goal} your Goal.")
            return
        for neighbour in tree[start]:
            dfs(neighbour, goal)
            if neighbour == goal:
                return
        stack.pop()

dfs('A',"E") 
print(f"Stack of nodes : {stack}") 
print()      