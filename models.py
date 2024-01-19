from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# database.py에서 정의한 Base 클래스 상속해서 만들어야 함
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True) # Integer이고, 기본키로 설정한 속성은 값이 자동으로 증가하는 특징이 있어 값 세팅안해도 1씩 증가하면서 저장됨
    subject = Column(String, nullable=False)  # String - 글자 수 제한
    content = Column(Text, nullable=False)  # Text - 글자 수 제한 x
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))  # question 테이블의 id 컬럼, question 객체의 속성 id 아님
    question = relationship("Question", backref="answers")  # answer.question.subject로 참조 가능, backref는 역참조(질문에 달린 답변들 참조 가능)

# alembic은 SQLAlchemy로 생성된 모델을 기반으로 데이터베이스 쉽게 관리해주는 도구, 테이블 생성하고 변경 가능
# migrations 내부에 테이블 생성 및 변경할 때마다 작업파일 (리비전) 생성됨


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)