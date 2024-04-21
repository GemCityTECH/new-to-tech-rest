from typing import Optional
from pydantic import BaseModel, conint

class Rating(BaseModel):
    rating: conint(ge=0, le=5)