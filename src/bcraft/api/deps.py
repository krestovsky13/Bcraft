from typing import Callable, Type, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from src.bcraft.api.models import Statistic
from src.bcraft.repository import BaseRepository
from src.bcraft.session import db_session


def get_repository(repo_type: Type[BaseRepository]) -> Callable:
    def get_repo(session: Session = Depends(db_session.get_session)) -> BaseRepository:
        return repo_type(session)
    return get_repo


def validate_query_params(sort_by: Optional[str] = 'date', order_by: Optional[str] = 'desc'):
    if sort_by in Statistic.__table__._columns.keys():
        if order_by:
            if order_by in ('asc', 'desc'):
                return sort_by, order_by
            else:
                raise HTTPException(status_code=400, detail=f"Query param {order_by} must be from the list ('asc', 'desc').")
        else:
            raise HTTPException(status_code=400, detail=f"Query param {order_by} empty.")
    else:
        raise HTTPException(status_code=400, detail=f"Query param {sort_by} not column of model.")
