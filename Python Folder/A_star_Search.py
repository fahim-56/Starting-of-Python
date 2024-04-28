graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('D', 1)],
    'C': [('E', 3)],
    'D': [('H', 2)],
    'E': [],
    'H': []
}

source_node = 'A'
goal_node = 'H'

def A_Star_Search(graph, source_node, goal_node, h):
    list = [(h(source_node, goal_node), 0, source_node)]
    cs = set()

    
     
    while list:
        list.sort()
        
        cu,curr_goal, curr_node = list.pop(0)

        if curr_node == goal_node:
            print("Goal :", curr_node)
            print("Total cost:", curr_goal)
            return
        else:
            cs.add(curr_node)

            for neighbor, cost in graph[curr_node]:
                if neighbor in cs:
                    continue
            
                neighbor_g = curr_goal + cost
                neighbor_f = neighbor_g + h(neighbor, goal_node)

                list.append((neighbor_f, neighbor_g, neighbor))

            print(curr_node)

    print("Goal not reached")


def Euclidean_Distance(node, goal_node):
    return abs(ord(node) - ord(goal_node))


A_Star_Search(graph, source_node, goal_node, Euclidean_Distance)