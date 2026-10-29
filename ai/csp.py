def csp_filter(books, preferences):
    """Apply user-specified fields as constraints; blank values are unrestricted."""
    results = []
    for book in books:
        if preferences.get("subject") and book.subject.lower() != preferences["subject"].lower():
            continue
        if preferences.get("category") and book.category.lower() != preferences["category"].lower():
            continue
        if preferences.get("level") and book.level.lower() != preferences["level"].lower():
            continue
        if preferences.get("language") and book.language.lower() != preferences["language"].lower():
            continue
        if preferences.get("available_only") and not book.available:
            continue
        results.append(book)
    return results
