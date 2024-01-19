1. main.py
: 전체 프로젝트 설정, FastAPI 프로젝트의 전체적인 환경을 설정하는 파일

2. database.py
: 데이터베이스와 관련된 설정을 하는 파일
: 데이터베이스를 사용하기 위한 변수, 함수 등을 정의하고 접속할 데이터베이스의 주소, 사용자, 비밀번호 등을 관리

3. models.py
: 모델 관리 파일
: SQLAlchemy(ORM을 지원하는 파이썬 데이터베이스 도구)는 모델 기반으로 데이터베이스를 처리함

4. domain.py
: API 구성하는 파일
: 해당 프로젝트는 질문과 답변을 작성하는 게시판을 만드는 것
: 질문, 답변, 사용자 라는 총 3개의 도메인을 두는 파일
: 각 도메인은 API를 생성하기 위해 해당 파일 필요
    1. 라우터 파일 - URL과 API의 전체적인 동작 관리
    2. 데이터베이스 처리 파일 : CRUD(데이터 생성, 조회, 수정, 삭제)
    3. 입출력 관리 파일 : 입력 데이터와 출력 데이터의 스펙 정의 및 검증
: ex) domain/question
    1. question_router.py : 라우터 파일
        - 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위
    2. question_crud.py : 데이터베이스 처리 파일
    3. question_schema.py : 입출력 관리 파일

5. frontend
: Svelte 프레임워크를 설치한 디렉토리. Svelte의 소스 및 빌드 파일들을 저장할 프론트엔드의 루트 디렉터리
: 최종적으로 frontend/dist 디렉터리에 생성된 빌드 파일들을 배포시에 사용할 것임임
: node 깔려있어야지 Svelte 사용 가능

myapi.db
: 리비전 파일 생성 -> 실행 -> question, answer 테이블 생성됨
: SQLite 데이터베이스의 데이터 파일

Pydantic
: FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리 (FastAPI 설치 시 자동 설치)
    1. 입출력 항목의 갯수와 타입을 설정
    2. 입출력 항목의 필수값 체크
    3. 입출력 항목의 데이터 검증

uvicorn
: FastAPI로 작성한 프로그램을 실행하기 위해서는 FastAPI 프로그램을 구동할 서버가 필요함
: 유비콘은 비동기 호출을 지원하는 파이썬용 웹 서버임

프론트엔드 서버 (Svelte 서버) 실행
: npm run dev

백엔드 서버 (FastAPI 서버) 실행
: uvicorn main:app --reload
