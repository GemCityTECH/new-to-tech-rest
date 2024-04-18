from pydantic import BaseModel


# Very simple schema for Review
# No constraints on rating int
# Assume unique submitter name
class Review(BaseModel):
    submitter: str
    rating: int
