from collections import deque

def bfs_state_space(graph, start_vertex):
    visited = []
    queue = deque([(start_vertex, [start_vertex])])
    paths = {start_vertex: [start_vertex]}
    
    while queue:
        current, path = queue.popleft()
        if current not in visited:
            visited.append(current)
            
        for neighbor in sorted(graph.get(current, [])):
            if neighbor not in paths:
                paths[neighbor] = path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
                
    return visited, paths

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B', 'E'],
        'E': ['C', 'D']
    }
    start_vertex = 'A'
    print("State-Space Search Problem using BFS")
    print(f"Start Vertex = {start_vertex}")
    
    visited_order, paths = bfs_state_space(graph, start_vertex)
    print("State-Space BFS Traversal Order:", " -> ".join(visited_order))
    print("Shortest Paths from Start Vertex:")
    for dest, path in sorted(paths.items()):
        print(f"Path to {dest}: {' -> '.join(path)} (Length: {len(path) - 1})")

if __name__ == '__main__':
    main()
