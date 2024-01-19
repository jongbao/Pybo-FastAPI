# python ORM 라이브러리
# ORM을 사용하면 sql 쿼리 없이, 파이썬 코드로 데이터 접근 및 처리 가능
# 데이터를 관리하는데 쓰는 파이썬 ORM 클래스를 모델이라고 함 (내부에서 쿼리 자동으로 생성)
# ORM을 사용하면 데이터베이스 종류에 상관없이 일관된 코드를 유지할 수 있어 프로그램 유지, 보수가 편함
# 또한 자동으로 쿼리 생성해주기 때문에 개발자가 달라고 통일된 쿼리를 작성할 수 있음
# import contextlib # Dependency Injection (의존성 주입)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlite는 파이썬 기본 패키지에 포함된 소규모 프로젝트에서 사용하는 데이터베이스
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

# 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 컨넥션 풀 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# 데이터베이스에 접속하기 위해 필요한 클래스
# autocommit = False -> commit 해야지만 실제 저장이 됨, True면 rollback 동작 안함
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# db 세션 객체를 생성하고 종료하는 반복 작업 제너레이터를 함수로 생성
# Depends 사용하면 자동으로 contextmanager가 적용되므로 제거해야함 (안그러면 이중적용)
# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()
