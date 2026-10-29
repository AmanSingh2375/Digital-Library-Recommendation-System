from dataclasses import dataclass, field
from typing import List

@dataclass
class Book:
    book_id: int
    title: str
    author: str
    subject: str
    category: str
    keywords: List[str]
    language: str
    level: str
    available: bool = True
    popularity: int = 0

    def searchable_text(self) -> str:
        return " ".join([
            self.title, self.author, self.subject, self.category,
            self.language, self.level, " ".join(self.keywords)
        ]).lower()
