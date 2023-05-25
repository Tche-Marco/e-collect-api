from sqlalchemy.orm import Session
from typing import List, Optional

import app.core.user.models as models
from app.core.user.schema import (
    UserCreate,
    UserUpdate,
    User,
)


def get_user(db: Session, user_id: int) -> Optional[User]:
    """
    Função para obter um usuário por id
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user is None:
        return None

    return User.from_orm(db_user)


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """
    Função para obter uma lista de usuários
    O parâmetro 'skip' pula um número de linhas, 'limit' limita o número total de linhas retornadas.
    """
    db_users = db.query(models.User).offset(skip).limit(limit).all()

    return [User.from_orm(db_user) for db_user in db_users]


def create_user(db: Session, user: UserCreate) -> User:
    """
    Função para criar um novo usuário
    """
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return User.from_orm(db_user)


def update_user(db: Session, user: UserUpdate, user_id: int) -> Optional[User]:
    """
    Função para atualizar um usuário
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user is None:
        return None

    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return User.from_orm(db_user)


def delete_user(db: Session, user_id: int) -> Optional[User]:
    """
    Função para deletar um usuário
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()

    return User.from_orm(db_user)
