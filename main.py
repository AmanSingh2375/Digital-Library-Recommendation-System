from data.library import load_books
from services.search_service import text_search, state_space_search, graph_search
from services.recommendation_service import recommend
from ai.state_space import build_library_state_space
from ai.bfs import bfs
from ai.dfs import dfs

def show_books(books):
    if not books:
        print("\\nNo matching books found.")
        return
    print("\\n" + "-" * 112)
    print(f"{'ID':<4}{'TITLE':<34}{'AUTHOR':<18}{'SUBJECT':<25}{'CATEGORY':<24}{'LEVEL':<14}{'STATUS'}")
    print("-" * 112)
    for b in books:
        status = "Available" if b.available else "Borrowed"
        print(f"{b.book_id:<4}{b.title[:32]:<34}{b.author[:16]:<18}{b.subject[:23]:<25}{b.category[:22]:<24}{b.level:<14}{status}")
    print("-" * 112)

def get_preferences():
    print("\\nEnter book preferences (press Enter to skip any field).")
    subject = input("Subject: ").strip()
    category = input("Category: ").strip()
    level = input("Level (Beginner/Intermediate/Advanced): ").strip()
    language = input("Language (English/Hindi): ").strip()
    keywords = [x.strip().lower() for x in input("Keywords (comma-separated): ").split(",") if x.strip()]
    available = input("Only available books? (Y/n): ").strip().lower()
    return {"subject": subject, "category": category, "level": level, "language": language,
            "keywords": keywords, "available_only": available != "n"}

def main():
    books = load_books()
    while True:
        print("""
=====================================================================
           DIGITAL LIBRARY RECOMMENDATION SYSTEM
                         TERMINAL MENU
=====================================================================
1. View all books
2. Search books by title/author/keyword
3. State Space Search by subject/category
4. BFS traversal demonstration
5. DFS traversal demonstration
6. Recommendations using CSP + Heuristic + Greedy
7. Recommendations using A* ranking
8. Exit
""")
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            show_books(books)
        elif choice == "2":
            q = input("Search term: ").strip()
            show_books(text_search(books, q))
        elif choice == "3":
            subject = input("Subject (blank for any): ").strip()
            category = input("Category (blank for any): ").strip()
            show_books(state_space_search(books, subject, category))
        elif choice in ("4", "5"):
            tree = build_library_state_space(books)
            graph = {"Library": list(tree["Library"].keys())}
            for subject, categories in tree["Library"].items():
                graph[subject] = list(categories.keys())
                for category, titles in categories.items():
                    graph[category] = list(titles)
            start = "Library"
            query = input("Optional target node/title (blank to show full traversal): ").strip()
            if query:
                target = next((node for node in graph if node.lower() == query.lower()), None)
                if target is None:
                    target = next((title for cats in tree["Library"].values() for titles in cats.values() for title in titles if title.lower() == query.lower()), None)
            else:
                target = None
            visited, path = (bfs if choice == "4" else dfs)(graph, start, target)
            print("\\nTraversal order:")
            print(" -> ".join(visited))
            if target:
                print("Path found:", " -> ".join(path) if path else "No path found.")
            print(f"Total nodes visited: {len(visited)}")
        elif choice == "6":
            prefs = get_preferences()
            candidates, ranked = recommend(books, prefs, "greedy")
            print(f"\\nCSP left {len(candidates)} candidate book(s).")
            if not candidates:
                print("No books match every constraint. Leave some preference fields blank and retry.")
            else:
                print("\\nRanked recommendations:")
                for item in ranked[:10]:
                    b = item["book"]
                    print(f"Score {item['score']:>2} | {b.title} — {b.author} | {b.subject} | {b.category}")
                    if item["reasons"]:
                        print("   Reasons:", "; ".join(item["reasons"]))
        elif choice == "7":
            prefs = get_preferences()
            candidates, ranked = recommend(books, prefs, "astar")
            print(f"\\nCSP left {len(candidates)} candidate book(s). A* ranking:")
            for item in ranked[:10]:
                b = item["book"]
                print(f"f={item['f']:>3} (g={item['g']}, h={item['h']}) | relevance={item['relevance']:>2} | {b.title}")
        elif choice == "8":
            print("Thank you for using Digital Library Recommendation System.")
            break
        else:
            print("Invalid option. Enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
