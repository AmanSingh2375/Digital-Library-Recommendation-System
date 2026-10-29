def build_library_state_space(books):
    """Build Library -> Subject -> Category -> Book-title hierarchy."""
    tree = {"Library": {}}
    for book in books:
        subject_node = tree["Library"].setdefault(book.subject, {})
        category_node = subject_node.setdefault(book.category, [])
        category_node.append(book.title)
    return tree

def find_in_state_space(tree, subject="", category=""):
    results = []
    subjects = tree.get("Library", {})
    for subject_name, categories in subjects.items():
        if subject and subject.lower() not in subject_name.lower():
            continue
        for category_name, titles in categories.items():
            if category and category.lower() not in category_name.lower():
                continue
            results.extend((subject_name, category_name, title) for title in titles)
    return results
