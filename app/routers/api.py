import logging
import schemas

from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, Query, HTTPException
from starlette import status

from database import get_db
from utils import upload_questions


router = APIRouter(prefix="/api", tags=["api"])
questions = []


@router.get("/home")
def read_root():
    return {"Hello": "World"}


@router.post(
    "/random",
    status_code=status.HTTP_201_CREATED,
    response_model=List[schemas.QuestionBase],
)
def questions_num(count: int = Query(..., ge=1), db: Session = Depends(get_db)):
    global questions
    try:
        upload_questions(db, count, questions)
        result = questions[:]
        questions.clear()
        return result
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=500, detail=e)
