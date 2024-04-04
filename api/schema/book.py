from typing import Optional

from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    publication_year: Optional[int] = None
    rating: Optional[int] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    def from_base(base: BookBase, id: int):
        return Book(
            id = id,
            title = base.title,
            author = base.author,
            publication_year = base.publication_year,
            rating = base.rating
        )