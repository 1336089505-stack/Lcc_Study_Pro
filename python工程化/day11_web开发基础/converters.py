from model import Question  # SQLAlchemy 实体类
from question_module import QuestionModel # Pydantic 模型

class QuestionConverter:
    @staticmethod
    def question_to_model(question: Question) -> QuestionModel:
        return QuestionModel.model_validate(question)

    @staticmethod
    def model_to_question(model: QuestionModel) -> Question:
        data = model.model_dump(exclude_unset = True)
        return Question(**data)

