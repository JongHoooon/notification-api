import sys
sys.path.append("..")

from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from database.conn import db
from database.schema import Users

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """
    # user = Users(status="active", name="HelloWorld")
    # session.add(user)
    # session.commit()
    
    # Users().create(session, auto_commit=True, name="bromp")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%y.%m.%d %H:%M:$S')})")