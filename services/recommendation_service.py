from ai.csp import csp_filter
from ai.greedy import greedy_best_first
from ai.astar import astar_rank

def recommend(books, preferences, algorithm="greedy"):
    candidates = csp_filter(books, preferences)
    if algorithm.lower() == "astar":
        return candidates, astar_rank(candidates, preferences)
    return candidates, greedy_best_first(candidates, preferences)
