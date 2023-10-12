import logging

from sqlalchemy.orm import Session

import models, schemas


def get_or_create_question(
    db: Session, question: schemas.QuestionCreate, category_id: int
) -> schemas.QuestionBase:
    try:
        question_obj = schemas.QuestionBase(**question)
        category_obj = question_obj.category

        db_category = (
            db.query(models.Category).filter(models.Category.id == category_id).first()
        )
        if not db_category:
            db_category = models.Category(**category_obj.dict())
            db.add(db_category)
            db.commit()
            db.refresh(db_category)
            logging.info("Category created, id {}".format(category_obj.id))
        else:
            db_category.updated_at = category_obj.updated_at
            db.commit()
            logging.info("Category updated, id {}".format(category_obj.id))

        db_question = (
            db.query(models.Question)
            .filter(models.Question.id == question_obj.id)
            .first()
        )
        if db_question:
            db_question.airdate = question_obj.airdate
            db_question.created_at = question_obj.created_at
            db_question.updated_at = question_obj.updated_at
            db.commit()
            db.refresh(db_question)
            logging.info("Question updated, id {}".format(question_obj.id))
            return schemas.QuestionBase(
                id=db_question.id,
                answer=db_question.answer,
                question=db_question.question,
                value=db_question.value,
                airdate=db_question.airdate,
                created_at=db_question.created_at,
                updated_at=db_question.updated_at,
                game_id=db_question.game_id,
                invalid_count=db_question.invalid_count,
                category_id=db_question.category_id,
                category=schemas.Category(**question_obj.category.dict()),
            )

        # del question_obj.category
        db_question = models.Question(**question_obj.dict(exclude={"category"}))
        db.add(db_question)
        db.commit()
        logging.info("Question created, id {}".format(question_obj.id))
        return schemas.QuestionBase(
            id=db_question.id,
            answer=db_question.answer,
            question=db_question.question,
            value=db_question.value,
            airdate=db_question.airdate,
            created_at=db_question.created_at,
            updated_at=db_question.updated_at,
            game_id=db_question.game_id,
            invalid_count=db_question.invalid_count,
            category_id=db_question.category_id,
            category=schemas.Category(**question_obj.category.dict()),
        )

    except Exception as exc:
        db.close()
        logging.exception(question)
        logging.exception(exc)
