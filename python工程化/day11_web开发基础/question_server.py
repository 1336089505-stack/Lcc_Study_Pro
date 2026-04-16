from question_module import QuestionModel
from question_repositories import QuestionRepository
from session import get_session
from converters import QuestionConverter
from model import Question


class QuestionServer:
    def __init__(self):
        pass

    def save(self, question: QuestionModel):
        with get_session() as session:
            que = QuestionRepository(session)
            entity = QuestionConverter.model_to_question(question)  # model to orm
            que.save(entity)
            session.commit()

    def delete(self, question_id: int):
        with get_session() as session:
            que = QuestionRepository(session)
            que.delete(question_id)
            session.commit()

    def get_all(self) :
        with get_session() as session:
            que = QuestionRepository(session)
            question_entity = que.find_all()

            return [QuestionConverter.question_to_model(entity) for entity in question_entity]

    def get_paginated(self, page: int, page_size: int):
        with get_session() as session:
            que = QuestionRepository(session)
            question_entity, total = que.find_paginated(page, page_size)
            models = [QuestionConverter.question_to_model(entity) for entity in question_entity]
            return models, total

    def search(self, keyword: str, page: int, page_size: int):
        with get_session() as session:
            que = QuestionRepository(session)
            question_entity, total = que.search(keyword, page, page_size)
            models = [QuestionConverter.question_to_model(entity) for entity in question_entity]
            return models, total

