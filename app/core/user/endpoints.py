from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from app.core.database import get_db

from app.core.user.schema import User, UserCreate, UserUpdate
from app.core.user.functions import (
    get_user,
    get_users,
    create_user,
    update_user,
    delete_user,
)


router = APIRouter()


@router.post("/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user.id)

    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe!")

    return create_user(db=db, user=user)


@router.get("/", response_model=List[User])
def get_users_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)

    return users


@router.get("/{user_id}", response_model=User)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")

    return db_user


@router.put("/{user_id}", response_model=User)
def update_user_route(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id=user_id, user=user)

    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")

    return db_user


@router.delete("/{user_id}", response_model=User)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")

    return db_user
