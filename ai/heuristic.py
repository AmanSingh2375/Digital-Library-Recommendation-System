def heuristic_score(book, preferences):
    """Estimate book relevance using the project's documented weighted rules."""
    score = 0
    reasons = []
    if preferences.get("subject") and preferences["subject"].lower() == book.subject.lower():
        score += 5
        reasons.append("subject match +5")
    if preferences.get("category") and preferences["category"].lower() == book.category.lower():
        score += 3
        reasons.append("category match +3")
    wanted = {word.lower() for word in preferences.get("keywords", [])}
    matches = wanted.intersection(word.lower() for word in book.keywords)
    if matches:
        score += 2 * len(matches)
        reasons.append(f"keyword match {sorted(matches)} +{2 * len(matches)}")
    if preferences.get("level") and preferences["level"].lower() == book.level.lower():
        score += 2
        reasons.append("level match +2")
    if preferences.get("language") and preferences["language"].lower() == book.language.lower():
        score += 1
        reasons.append("language match +1")
    if book.available:
        score += 1
        reasons.append("available +1")
    return score, reasons
