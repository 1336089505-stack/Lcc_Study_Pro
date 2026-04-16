from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from model import Question


class QuestionRepository:
    def __init__(self,session:Session):
        self.session = session

    def save(self, question: Question):
        self.session.add(question)

    def delete(self, question_id: int):
        question = self.find_by_id(question_id)
        if question:
            self.session.delete(question)

    def find_by_id(self, question_id: int):
        return self.session.get(Question, question_id)

    def find_all(self):
        statement = select(Question)
        result = self.session.scalars(statement)
        questions = result.all()
        return questions

    def find_paginated(self, page: int, page_size: int):
        offset = (page - 1) * page_size
        statement = select(Question).offset(offset).limit(page_size)
        result = self.session.scalars(statement)
        questions = result.all()
        
        # Count total questions
        count_statement = select(Question)
        total = len(self.session.scalars(count_statement).all())
        
        return questions, total

    def search(self, keyword: str, page: int, page_size: int):
        offset = (page - 1) * page_size
        search_pattern = f"%{keyword}%"
        statement = select(Question).where(
            or_(
                Question.title.ilike(search_pattern),
                Question.content.ilike(search_pattern),
                Question.tags.ilike(search_pattern)
            )
        ).offset(offset).limit(page_size)
        result = self.session.scalars(statement)
        questions = result.all()
        
        # Count total matching questions
        count_statement = select(Question).where(
            or_(
                Question.title.ilike(search_pattern),
                Question.content.ilike(search_pattern),
                Question.tags.ilike(search_pattern)
            )
        )
        total = len(self.session.scalars(count_statement).all())
        
        return questions, total