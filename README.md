# Digital Library Recommendation System — Terminal Version

A terminal-based Python project demonstrating AI search and recommendation concepts relevant to the Digital Library Recommendation System.

## Run in VS Code
1. Extract the ZIP.
2. Open the `Digital_Library_Terminal_Advanced` folder in VS Code.
3. Open a terminal in this folder.
4. Run:

```bash
py main.py
```

If `py` is unavailable, use `python main.py`.

**Requirements:** Python 3.10+; standard library only, no `pip install` needed.

## Folder structure

```text
Digital_Library_Terminal_Advanced/
├── main.py
├── models.py
├── data/
│   ├── books.json
│   └── library.py
├── ai/
│   ├── state_space.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── heuristic.py
│   ├── greedy.py
│   ├── astar.py
│   └── csp.py
├── services/
│   ├── search_service.py
│   └── recommendation_service.py
└── README.md
```

## Concepts demonstrated
- State-space hierarchy: Library → Subject → Category → Book
- BFS: breadth-first graph traversal
- DFS: depth-first graph traversal
- Heuristic scoring: subject +5, category +3, matching keyword +2 each, level +2, language +1, availability +1
- Greedy ranking: prioritizes highest heuristic score
- A* educational ranking: `f(n) = g(n) + h(n)` with a mismatch penalty and relevance-based heuristic
- CSP-style filtering: subject, category, level, language and availability constraints

## Notes
- The sample catalogue is stored in `data/books.json`; edit it to add books.
- This version uses JSON file storage, not a database server.
- The A* module is an educational ranking demonstration, not a claim of globally optimal recommendations.
- BFS and DFS are implemented as separate modules so their code can be shown independently in a viva.
