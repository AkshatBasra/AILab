def DLS(graph, node, limit, goal, path):
    if node == goal:
        return path
    if limit <= 0:
        return None
    if node in graph:
        for neighbour in graph[node]:
            new_path = path.copy()
            new_path.append(neighbour)
            result = DLS(graph, neighbour, limit - 1, goal, new_path)
            if result is not None:
                return result
            

def IDDFS(graph, start, goal):
    depth = 0
    while True:
        path = DLS(graph, start, depth, goal, [start])
        if path is not None:
            return path
        depth += 1

my_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J'],
        'F': ['K']
    }

start_node = 'A'
goal_node = 'K'

shortest_path = IDDFS(my_graph, start_node, goal_node)

if shortest_path:
    print("Shortest path found:", shortest_path)
else:
    print("No path found.")
