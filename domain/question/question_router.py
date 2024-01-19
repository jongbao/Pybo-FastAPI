from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_schema, question_crud
# from models import Question

# router 객체를 생성하여 FastAPI앱에 등록해야지 라우팅 기능 사용 가능
router = APIRouter(
    prefix="/api/question", # url에 항상 포함되어야 하는 값
)


# @router.get("/list")
# def question_list():
#     db = SessionLocal() # db 세션 생성
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close() # 세션 컨넥션 풀에 반환 (종료 x)
#     return _question_list

# question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미함
@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                  page: int = 0, size: int = 10): # with문 없이 간편 실행
    # 오류에 상관없이 with문 벗어나는 순간 db.close()가 실행됨
    # with get_db() as db:
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)