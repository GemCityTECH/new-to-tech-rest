from typing import Optional
from pydantic import BaseModel, conint

class Review(BaseModel):
    reviewer: Optional[str] = None
    review: Optional[str] = None
    rating: Optional[conint(ge=0, le=5)] = None