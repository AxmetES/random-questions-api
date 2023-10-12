import logging

import schemas
import requests

from sqlalchemy.orm import Session
from typing import List

import crud
from config import settings


def upload_questions(
    db: Session, questions_num: int, questions: list
) -> List[schemas.QuestionBase]:
    try:
        questions_url = settings.QUESTIONS_URL.format(questions_num)
        r = requests.get(url=questions_url)
        logging.info(f'jservice.io status: {r.status_code}')
        logging.info(f'response from jservice.io: {r.text}')
        r.raise_for_status()
        for question in r.json():
            q_response = crud.get_or_create_question(
                db, question, question["category"]["id"]
            )
            if q_response:
                questions.append(q_response)
                questions_num -= 1
            else:
                return upload_questions(db, questions_num)
    except Exception as e:
        logging.exception(e)