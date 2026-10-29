from ai.state_space import build_library_state_space, find_in_state_space
from ai.bfs import bfs
from ai.dfs import dfs

def make_graph(books):
    """Convert library hierarchy into a graph for BFS/DFS."""
    tree = build_library_state_space(books)
    graph = {"Library": list(tree["Library"].keys())}
    for subject, categories in tree["Library"].items():
        graph[subject] = list(categories.keys())
        for category, titles in categories.items():
            graph[category] = list(titles)
    return graph

def text_search(books, query):
    q = query.strip().lower()
    if not q:
        return []
    return [b for b in books if q in b.searchable_text()]

def state_space_search(books, subject="", category=""):
    tree = build_library_state_space(books)
    triples = find_in_state_space(tree, subject, category)
    wanted = {title for _, _, title in triples}
    return [b for b in books if b.title in wanted]

def graph_search(books, query, algorithm="bfs"):
    graph = make_graph(books)
    algo = bfs if algorithm.lower() == "bfs" else dfs
    visited, _ = algo(graph, "Library")
    # Search book fields too, so the interface supports author/keyword queries.
    results = text_search(books, query)
    return results, visited
