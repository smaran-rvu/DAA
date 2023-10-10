import os
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def min_edges_bfs(self, source, destination):
        visited = set()
        queue = deque([(source, 0)])  # (vertex, distance)

        while queue:
            vertex, distance = queue.popleft()
            visited.add(vertex)

            if vertex == destination:
                return distance

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

        return -1  # No path found
        
no_vertices = int(input())
if no_vertices == 0:
    print(-1)
    os._exit(1)

no_edges = int(input())
edges = []

if no_edges == 0:
    print(-1)
    os._exit(1)

for i in range(no_edges):
    edges.append(eval(input()))

g = Graph()
for u, v in edges:
    g.add_edge(u, v)

source, destination = eval(input())
min_edges = g.min_edges_bfs(source, destination)
print(min_edges)