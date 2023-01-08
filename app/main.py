from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI
from database.conn import db
from common.config import conf
from routes import index, auth

def create_app():
    """
    앱 함수 실행
    :return:
    """
    
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    
    # 라우터 정의
    app.include_router(index.router)
    app.include_router(auth.router, 
                       tags=["Authentication"],
                       prefix="/auth")
    
    return app


app = create_app()


# 다른 파일에서 실행하면 이 파일 실행 안된다.
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)


