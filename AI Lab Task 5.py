# Name: Fatima            BSAI(3A)
# Roll no: SU92-BSAIM-S25-025
# Task 4:

# DFS using Stack (Iterative)

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbors in reverse order for correct DFS order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


# Graph representation (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

dfs_stack(graph, 'A')