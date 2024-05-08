from collections import deque

def bfs(graph, source):

  n = len(graph)
  visited = [False] * n

  queue = deque([source])
  visited[source] = True

  while queue:
    current_node = queue.popleft()
    print(current_node, end=" ")
    for neighbor in graph[current_node]:
      if not visited[neighbor]:
        queue.append(neighbor)
        visited[neighbor] = True

# Example usage
if __name__ == "__main__":
  n, e = map(int, input("Enter number of nodes and edges: ").split())
  graph = [[] for _ in range(n)]  # Initialize adjacency list

  for _ in range(e):
    u, v = map(int, input("Enter edge (node1 node2): ").split())
    graph[u].append(v)
    graph[v].append(u)  # Handle undirected graph

  source = int(input("Enter source node: "))
  bfs(graph, source)
