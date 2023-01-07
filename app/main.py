import uvicorn
from fastapi import FastAPI
from app.common.config import conf

def create_app():
    """
    앱 함수 실행
    :return:
    """
    
    c = conf()
    app = FastAPI()
    
    
    return app


app = create_app()


# 다른 파일에서 실행하면 이 파일 실행 안된다.
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)


