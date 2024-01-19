import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer


# 정해진 타입이 아닌 다른 타입의 자료형이 대입되면 오류가 발생함
# 만약 subject가 필수항목이 아니게 설정하려면 subject : str | None = None
class Question(BaseModel):
    id : int
    subject : str
    content : str
    create_date : datetime.datetime
    answers: list[Answer] = []


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []