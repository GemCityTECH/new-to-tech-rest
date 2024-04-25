from typing import Optional, List
from pydantic import BaseModel
from .review import Review
import statistics

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: Optional[int] = None
    reviews: List[Review] = []

    def avg_rating(self) -> float:
        ratings = [review.rating for review in self.reviews if review.rating is not None]
        if not ratings:
            return 0.0
        return statistics.mean(ratings)
    
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
            reviews = base.reviews
        )
    

# TODO You may need to create new class(es) inheriting BaseModel in order to implement the 'multiple ratings' feature.
# BaseModel is from Pydantic - see docs at https://docs.pydantic.dev/latest/concepts/models/
# Think carefully about how to structure the classes and endpoints for this feature!