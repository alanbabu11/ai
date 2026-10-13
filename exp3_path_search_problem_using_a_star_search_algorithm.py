def a_star_search(graph, heuristics, start, goal):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parents = {start: start}

    while open_set:
        # Pick node n in open_set with minimum f(n) = g(n) + h(n)
        curr = min(open_set, key=lambda n: g[n] + heuristics.get(n, float('inf')))

        if curr == goal:
            path = []
            while parents[curr] != curr:
                path.append(curr)
                curr = parents[curr]
            path.append(start)
            return path[::-1]

        open_set.remove(curr)
        closed_set.add(curr)

        for neighbor, weight in graph.get(curr, []):
            cost = g[curr] + weight
            if neighbor in closed_set:
                continue
            if neighbor not in open_set or cost < g.get(neighbor, float('inf')):
                parents[neighbor] = curr
                g[neighbor] = cost
                open_set.add(neighbor)

    return None


# Graph representation with edge costs
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

heuristics = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
path = a_star_search(Graph_nodes, heuristics, 'A', 'G')
print(f"Path found: {path}")
