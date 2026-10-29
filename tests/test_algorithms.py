import unittest
from models import Book
from ai.bfs import bfs
from ai.dfs import dfs
from ai.csp import csp_filter
from ai.heuristic import heuristic_score

class TestLibraryAlgorithms(unittest.TestCase):
    def setUp(self):
        self.graph = {"Library": ["CS", "Physics"], "CS": ["Programming"], "Programming": ["Python Basics"], "Physics": ["Physics Basics"]}
        self.books = [
            Book(1, "Python Basics", "A", "Computer Science", "Programming", ["python", "coding"], "English", "Beginner", True, 5),
            Book(2, "Physics Basics", "B", "Physics", "Science", ["motion"], "English", "Beginner", True, 3),
        ]

    def test_bfs_finds_target(self):
        visited, path = bfs(self.graph, "Library", "Python Basics")
        self.assertIn("Python Basics", visited)
        self.assertEqual(path[0], "Library")
        self.assertEqual(path[-1], "Python Basics")

    def test_dfs_finds_target(self):
        visited, path = dfs(self.graph, "Library", "Physics Basics")
        self.assertIn("Physics Basics", visited)
        self.assertEqual(path[-1], "Physics Basics")

    def test_csp_subject_filter(self):
        prefs = {"subject": "Physics", "category": "", "level": "", "language": "", "available_only": True}
        self.assertEqual([b.title for b in csp_filter(self.books, prefs)], ["Physics Basics"])

    def test_heuristic_subject_score(self):
        prefs = {"subject": "Computer Science", "category": "", "keywords": [], "level": "", "language": ""}
        score, _ = heuristic_score(self.books[0], prefs)
        self.assertEqual(score, 6)  # subject match +5 and available +1

if __name__ == "__main__":
    unittest.main()
