import json
from pathlib import Path
from models import Book

DATA_FILE = Path(__file__).resolve().parent / "books.json"

def load_books():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        rows = json.load(file)
    return [Book(**row) for row in rows]

def save_books(books):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([book.__dict__ for book in books], file, indent=2, ensure_ascii=False)
