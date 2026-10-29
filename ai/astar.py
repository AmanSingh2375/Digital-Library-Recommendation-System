from ai.heuristic import heuristic_score

def astar_rank(books, preferences):
    """Educational A*-style ranking: f(n) = g(n) + h(n).

    g(n) is a mismatch penalty for subject/category. h(n) is negative
    relevance so that a smaller f value prioritizes more relevant candidates.
    This is a ranking demonstration, not a shortest-path optimality claim.
    """
    results = []
    for book in books:
        g = 0
        if preferences.get("subject") and preferences["subject"].lower() != book.subject.lower():
            g += 5
        if preferences.get("category") and preferences["category"].lower() != book.category.lower():
            g += 3
        relevance, reasons = heuristic_score(book, preferences)
        h = -relevance
        results.append({"book": book, "g": g, "h": h, "f": g + h,
                        "relevance": relevance, "reasons": reasons})
    return sorted(results, key=lambda item: (item["f"], -item["relevance"]))
