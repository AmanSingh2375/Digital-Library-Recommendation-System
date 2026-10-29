from collections import deque

def bfs(graph, start, target=None):
    """Breadth-First Search: visit graph nodes level by level."""
    queue = deque([start])
    visited = []
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.append(node)
        if target is not None and node == target:
            break
        for neighbour in graph.get(node, []):
            if neighbour not in parent:
                parent[neighbour] = node
                queue.append(neighbour)
    path = []
    if target is not None and target in visited:
        cur = target
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
    return visited, path
