from typing import Optional

from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    publication_year: Optional[int] = None
    rating: Optional[int] = None
    genre: str

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
            author = base.author,
            publication_year = base.publication_year,
            rating = base.rating,
            genre = base.genre
        )
    

# TODO You may need to create new class(es) inheriting BaseModel in order to implement the 'multiple ratings' feature.
# BaseModel is from Pydantic - see docs at https://docs.pydantic.dev/latest/concepts/models/
# Think carefully about how to structure the classes and endpoints for this feature!