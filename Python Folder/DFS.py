def DFS(graph, n, visited):
  
  visited[n] = True
  print(n, end=" ")  # Print the current node

  for child in graph[n]:
    if not visited[child]:
      DFS(graph, child, visited)

# Main program
n, e = map(int, input("Enter number of nodes and edges: ").split())  # Get input from user

graph = {i: [] for i in range(n)}  # Initialize an empty dictionary for the graph

# Build the graph (undirected)
for _ in range(e):
  a, b = map(int, input("Enter edge (a, b): ").split())
  graph[a].append(b)
  graph[b].append(a)

# Get the source node
src = int(input("Enter source node: "))

# Initialize visited list
visited = [False] * n

# Perform DFS traversal
DFS(graph, src, visited)
