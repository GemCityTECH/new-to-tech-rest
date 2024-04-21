from typing import Optional
from pydantic import BaseModel

class Review(BaseModel):
    review: str