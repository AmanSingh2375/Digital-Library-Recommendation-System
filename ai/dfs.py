def dfs(graph, start, target=None):
    """Depth-First Search: explore a branch deeply before backtracking."""
    stack = [start]
    visited = []
    parent = {start: None}
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        if target is not None and node == target:
            break
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in parent:
                parent[neighbour] = node
                stack.append(neighbour)
    path = []
    if target is not None and target in visited:
        cur = target
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
    return visited, path
