graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2)],
    'C': [('E', 4)],
    'D': [('F', 1)],
    'E': [],
    'F': []
}
sn = 'A'
gn = 'F'

def euclidean_distance(n, g):
    return abs(ord(n) - ord(g))

def Best_First_Search(graph, s, g, h):
    pq = [(h(s, g), s)]
    visited = set()

    while pq:
        pq.sort()
        current_cost, current_node = pq.pop(0)
        if current_node == g:
            print("Goal reached:", current_node)
            return
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                neighbor_cost = h(neighbor, g)
                pq.append((neighbor_cost, neighbor))
                visited.add(neighbor)

        print("Visited node:", current_node)
    print("Goal not reached")


Best_First_Search(graph, sn, gn, euclidean_distance)