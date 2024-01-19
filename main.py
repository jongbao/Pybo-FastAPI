from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router
from domain.answer import answer_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/hello") # /hello 라는 url 요청이 발생하면 해당 함수를 실행하여 결과를 리턴하라는 의미
# def hello():
#     return {"message": "안녕하세요 파이보"}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)