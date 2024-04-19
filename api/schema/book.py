from enum import Enum
from typing import Optional
from schema.review import Review
from statistics import mean

from pydantic import BaseModel, computed_field


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
    reviews: list[Review] = []

    @computed_field
    @property
    def average_rating(self) -> float:
        return round(mean(review.rating for review in self.reviews), 2)


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
            reviews=base.reviews,
        )
