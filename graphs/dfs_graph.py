"""
Depth first search for a graph.
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


# iterative approach
def dfs_iterative(graph, start):
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

