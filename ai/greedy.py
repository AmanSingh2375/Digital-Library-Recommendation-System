from ai.heuristic import heuristic_score

def greedy_best_first(books, preferences):
    """Prioritize the book with the highest heuristic relevance score."""
    ranked = []
    for book in books:
        score, reasons = heuristic_score(book, preferences)
        ranked.append({"book": book, "score": score, "reasons": reasons})
    return sorted(ranked, key=lambda item: (item["score"], item["book"].popularity), reverse=True)
