import heapq
import networkx as nx


def a_star_search(graph, start, goal, heuristic):
    # Priority queue: elements are tuples (f_score, count, node)
    frontier = []
    entry_count = 0
    # g_score: cost from start to n
    g_score = {start: 0}
    # came_from: parent pointers
    came_from = {}

    # initialize frontier with start node
    start_h = heuristic[start] if isinstance(heuristic, dict) else heuristic(start)
    heapq.heappush(frontier, (start_h, entry_count, start))
    entry_count += 1

    while frontier:
        current_f, _, current = heapq.heappop(frontier)

        # goal check
        if current == goal:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[goal]

        # expand neighbors
        for neighbor in graph.neighbors(current):
            edge_data = graph.get_edge_data(current, neighbor)
            weight = edge_data.get('weight', 1)
            tentative_g = g_score[current] + weight

            # if this path to neighbor is better
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                h = heuristic[neighbor] if isinstance(heuristic, dict) else heuristic(neighbor)
                f_score = tentative_g + h
                heapq.heappush(frontier, (f_score, entry_count, neighbor))
                entry_count += 1

    # failure
    return None, float('inf')


if __name__ == '__main__':
    # Định nghĩa đồ thị
    G = nx.Graph()
    edges = [
        ('S', 'A', 3),
        ('S', 'B', 9),
        ('S', 'C', 9),
        ('A', 'B', 4),
        ('A', 'D', 5),
        ('B', 'C', 4),
        ('B', 'D', 4),
        ('B', 'E', 3),
        ('C', 'F', 7),
        ('C', 'G', 4),
        ('D', 'E', 3),
        ('E', 'G', 3),
        ('F', 'G', 5)
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Heuristic values từ ví dụ (ước lượng đến G)
    heuristic = {
        'S': 10,
        'A': 8,
        'B': 5,
        'C': 8,
        'D': 4,
        'E': 3,
        'F': 4,
        'G': 0
    }

    start_node = 'S'
    goal_node = 'G'

    path, cost = a_star_search(G, start_node, goal_node, heuristic)
    if path:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")
