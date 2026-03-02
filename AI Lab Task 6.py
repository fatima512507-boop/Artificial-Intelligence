# Name: Fatima              BsAI(3A)
# Roll no: SU92-BSAIM-S25-025
# Task 6:

def bfs_simple(graph, start):
    visited = []
    queue = [start]   

    visited.append(start)

    while queue:
        node = queue.pop(0)   
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs_simple(graph, 'A')