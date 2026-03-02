# Name: Fatima       BSAI(3A)
# Roll no: SU92-BSAIM-S25-025
# Task 7:


def a_star(graph, heuristic, start, goal):
    open_list = [start]
    closed_list = set()

    g = {start: 0}
    parent = {start: None}

    while open_list:
        # Find node with lowest f(n)
        current = min(open_list, key=lambda node: g[node] + heuristic[node])

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            new_g = g[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif new_g >= g.get(neighbor, float('inf')):
                continue

            g[neighbor] = new_g
            parent[neighbor] = current

    return None


# Graph (Adjacency List with cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values (estimated distance to goal D)
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

path = a_star(graph, heuristic, 'A', 'D')
print("Shortest Path:", path)