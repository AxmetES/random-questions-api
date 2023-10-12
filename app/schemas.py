from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    clues_count: int


class Category(CategoryBase):
    pass


class QuestionBase(BaseModel):
    id: int
    answer: str
    question: str
    value: int | None = None
    airdate: datetime
    created_at: datetime
    updated_at: datetime
    game_id: int
    invalid_count: Optional[int]
    category_id: int
    category: Category


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass
