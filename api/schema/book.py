from typing import Optional
from pydantic import BaseModel
from .rating import Rating
import statistics

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: Optional[int] = None
    #rating: Optional[int] = None

    def avg_rating(sum_of_ratings) -> float:
        return statistics.mean(sum_of_ratings)

    # TODO
    # Add a 'genre' field here. You'll need to add it in a few other places as well!
    # Bonus: try implementing genre as an enum rather than a string

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    def from_base(base: BookBase, id: int):
        return Book(
            id = id,
            title = base.title,
            genre = base.genre,
            author = base.author,
            publication_year = base.publication_year,
            rating = base.rating
        )
    

# TODO You may need to create new class(es) inheriting BaseModel in order to implement the 'multiple ratings' feature.
# BaseModel is from Pydantic - see docs at https://docs.pydantic.dev/latest/concepts/models/
# Think carefully about how to structure the classes and endpoints for this feature!