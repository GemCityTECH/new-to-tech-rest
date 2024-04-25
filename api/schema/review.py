from typing import Optional
from pydantic import BaseModel, conint

class ReviewBase(BaseModel):
    reviewer: Optional[str] = None
    review: Optional[str] = None
    rating: Optional[conint(ge=0, le=5)] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    def from_base(base: ReviewBase, id: int):
        return Review(
            id = id,
            reviewer = base.reviewer,
            rewview = base.review,
            rating = base.rating
        )