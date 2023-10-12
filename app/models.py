from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)
    clues_count = Column(Integer)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)
    airdate = Column(DateTime)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)
    game_id = Column(Integer, index=True)
    invalid_count = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"), index=True)

    category = relationship("Category")
