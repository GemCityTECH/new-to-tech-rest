from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Genre(str, Enum):
    scifi = "Science Fiction"
    biography = "Biography"
    fantasy = "Fantasy"
    historical_fiction = "Historical Fiction"


class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[Genre]
    publication_year: Optional[int] = None
    rating: Optional[int] = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    def from_base(base: BookBase, id: int):
        return Book(
            id=id,
            title=base.title,
            author=base.author,
            genre=base.genre,
            publication_year=base.publication_year,
            rating=base.rating,
        )


# TODO You may need to create new class(es) inheriting BaseModel in order to implement the 'multiple ratings' feature.
# BaseModel is from Pydantic - see docs at https://docs.pydantic.dev/latest/concepts/models/
# Think carefully about how to structure the classes and endpoints for this feature!
